from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from catalog.models import Product


def home(request):
    """Контроллер для главной страницы"""
    return render(request, "home.html")


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


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


class ProductListView(ListView):
    """ Класс для представления объектов класса 'Product' """
    model = Product


# def products_list(request):
#     """Контроллер для отображения всех продуктов на страницу 'Главная'"""
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


class ProductDetailView(DetailView):
    """ Выводит представление отдельного объекта класса 'Product' """
    model = Product

# def product_detail(request, pk):
#     """Контроллер для отображения всей информации по одному продукту на странице 'Информация о товаре'"""
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
