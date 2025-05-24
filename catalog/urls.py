from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactsView, ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("contacts/", ContactsView.as_view(), name="feedback_form"),
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
