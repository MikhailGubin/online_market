from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog_app.models import Blog


class BlogListView(ListView):
    """ Класс для представления объектов класса 'Product' """
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    """ Выводит представление отдельного объекта класса 'Product' """
    model = Blog
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    """ Создаёт представление объекта класса 'Product' """
    model = Blog
    fields = ("title", "content", "preview", "publication_sign", "views_number")
    success_url = reverse_lazy("blog_app:blog_list")


class BlogUpdateView(UpdateView):
    """ Создаёт представление объекта класса 'Product' """
    model = Blog
    fields = ("title", "content", "preview", "publication_sign", "views_number")
    success_url = reverse_lazy("blog_app:blog_list")


class BlogDeleteView(DeleteView):
    """ Создаёт представление объекта класса 'Product' """
    model = Blog
    success_url = reverse_lazy("blog_app:blog_list")
