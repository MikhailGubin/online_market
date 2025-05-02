from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, feedback_form, home

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("contacts/", feedback_form, name="feedback_form"),
]
