from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog_app.forms import BlogForm
from blog_app.models import Blog


class BlogListView(ListView):
    """Класс для представления объектов класса 'Blog'"""

    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    """Выводит представление отдельного объекта класса 'Blog'"""

    model = Blog
    context_object_name = "blog"

    def get_object(self, queryset=None):
        """Добавляет количество просмотров к полю 'views_counter'"""
        self.blog = super().get_object(queryset)
        self.blog.views_counter += 1
        self.blog.save()
        return self.blog


class BlogCreateView(CreateView):
    """Создаёт представление объекта класса 'Blog'"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog_app:blog_list")


class BlogUpdateView(UpdateView):
    """Создаёт представление объекта класса 'Blog'"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog_app:blog_list")

    def get_success_url(self):
        """Перенаправлять пользователя на просмотр этой статьи после успешного редактирования записи"""
        return reverse("blog_app:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    """Создаёт представление объекта класса 'Blog'"""

    model = Blog
    success_url = reverse_lazy("blog_app:blog_list")
