from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from catalog.models import Product


def home(request):
    """Контроллер для главной страницы"""
    return render(request, "home.html")


def contacts(request):
    """Контроллер для страницы 'Контакты'"""
    return render(request, "contacts.html")


def feedback_form(request):
    """Контроллер для обработки обратной связи со страницы 'Контакты'"""

    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Обработка данных
        print(f"Получено новое сообщение от {name} ({phone}): \n{message}")
        return redirect("/")
    return render(request, "contacts.html")


def products_list(request):
    """Контроллер для отображения всех продуктов на страницу 'Главная'"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    """ Контроллер для отображения всей информации по одному продукту на странице 'Информация о товаре' """
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
