from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import get_product_from_cache


# def home(request):
#     """Контроллер для главной страницы"""
#     return render(request, "home.html")


# def contacts(request):
#     """Контроллер для страницы 'Contacts'"""
#     return render(request, "contacts.html")


# def feedback_form(request):
#     """Контроллер для обработки обратной связи со страницы 'Contacts'"""
#
#     if request.method == "POST":
#         # Получение данных из формы
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         # Обработка данных
#         print(f"Получено новое сообщение от {name} ({phone}): \n{message}")
#         return redirect("/")
#     return render(request, "contacts.html")


# def products_list(request):
#     """Контроллер для отображения всех продуктов на страницу 'Главная'"""
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


# def product_detail(request, pk):
#     """Контроллер для отображения всей информации по одному продукту на странице 'Информация о товаре'"""
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создаёт представление объекта класса 'Product'"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    """Класс для представления объектов класса 'Product'"""

    model = Product
    context_object_name = "products"

    def get_queryset(self):
        """ Выводит на экран только продукты с активным статусом публикации """
        queryset = super().get_queryset()
        user = self.request.user

        if user.has_perm("catalog.can_unpublish_product"):
            return queryset

        return queryset.filter(publish_product=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Выводит представление отдельного объекта класса 'Product'"""

    model = Product
    context_object_name = "product"

    def get_object(self, queryset=None):
        """Добавляет количество просмотров к полю 'views_counter'"""
        self.product = super().get_object(queryset)
        self.product.views_counter += 1
        self.product.save()
        return self.product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Создаёт представление объекта класса 'Product'"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        """
        Перенаправлять пользователя на просмотр этого товара после успешного редактирования информации этого товара
        """
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm

        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm

        raise PermissionDenied


class UnpublishProductView(LoginRequiredMixin, DeleteView):

    model = Product
    success_url = reverse_lazy("catalog:products_list")
    template_name = "catalog/product_confirm_unpublish.html"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "У вас нет прав для отмены публикации продукта."
            )

        product.publish_product = False
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Создаёт представление объекта класса 'Product'"""

    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = self.request.user
        if user.has_perm("catalog.can_delete_any_product") or user == product.owner:
            product.delete()
            return redirect("catalog:products_list")

        return HttpResponseForbidden(
            "У вас нет прав для удаления информации о продукте."
        )


class ContactsView(TemplateView):
    """Контроллер для отображения страницы 'Contacts'"""

    template_name = "catalog/contacts.html"
