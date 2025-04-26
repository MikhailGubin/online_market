from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, feedback_form

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("contacts/", feedback_form, name="feedback_form"),
]
