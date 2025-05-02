from django.contrib import admin
from django.contrib.admin import ModelAdmin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name',]


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ('category',)
    search_fields = ('name', 'description',)
