from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import (BlogDetailView,
                           BlogListView)

app_name = BlogAppConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="products_list"),
    path("/<int:pk>/", BlogDetailView.as_view(), name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)