from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog_app.models import Blog


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "preview",
        "publication_sign",
        "created_at",
        "views_counter",
    ]
    list_filter = ("title", "publication_sign", "created_at", "views_counter")
    search_fields = ("title", "created_at", "views_counter")
