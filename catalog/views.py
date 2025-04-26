from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    """ Контроллер для главной страницы """
    return render(request, "home.html")


def contacts(request):
    """ Контроллер для страницы 'Контакты' """
    return render(request, "contacts.html")


def feedback_form(request):
    """ Контроллер для обработки обратной связи со страницы 'Контакты' """

    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных
        print(f"Получено новое сообщение от {name} ({phone}): \n{message}")
        return redirect('/')
    return render(request, 'contacts.html')
