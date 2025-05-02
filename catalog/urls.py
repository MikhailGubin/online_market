from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, feedback_form, home

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("contacts/", feedback_form, name="feedback_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
