from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                            BlogListView, BlogUpdateView)

app_name = BlogAppConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("new/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
