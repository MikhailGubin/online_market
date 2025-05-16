from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import (BlogDetailView, BlogCreateView,
                           BlogListView)

app_name = BlogAppConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)