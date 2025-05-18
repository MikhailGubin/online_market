from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog_app.models import Blog


class BlogListView(ListView):
    """ Класс для представления объектов класса 'Blog' """
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    """ Выводит представление отдельного объекта класса 'Blog' """
    model = Blog
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.blog = super().get_object(queryset)
        self.blog.views_counter += 1
        self.blog.save()
        return self.blog


class BlogCreateView(CreateView):
    """ Создаёт представление объекта класса 'Blog' """
    model = Blog
    fields = ("title", "content", "preview", "publication_sign", "views_counter")
    success_url = reverse_lazy("blog_app:blog_list")


class BlogUpdateView(UpdateView):
    """ Создаёт представление объекта класса 'Blog' """
    model = Blog
    fields = ("title", "content", "preview", "publication_sign", "views_counter")
    success_url = reverse_lazy("blog_app:blog_list")

    def get_success_url(self):
        return reverse('blog_app:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """ Создаёт представление объекта класса 'Blog' """
    model = Blog
    success_url = reverse_lazy("blog_app:blog_list")
