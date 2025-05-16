from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from blog_app.models import Blog


class BlogListView(ListView):
    """ Класс для представления объектов класса 'Product' """
    model = Blog


class BlogDetailView(DetailView):
    """ Выводит представление отдельного объекта класса 'Product' """
    model = Blog



