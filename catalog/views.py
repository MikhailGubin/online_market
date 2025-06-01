from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product

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


class ProductListView(ListView):
    """Класс для представления объектов класса 'Product'"""

    model = Product
    context_object_name = "products"


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

        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_any_product"):
            return ProductModeratorForm

        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Создаёт представление объекта класса 'Product'"""

    model = Product
    success_url = reverse_lazy("catalog:products_list")


class ContactsView(TemplateView):
    """Контроллер для отображения страницы 'Contacts'"""

    template_name = "catalog/contacts.html"
