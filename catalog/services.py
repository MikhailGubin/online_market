from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


class ProductService:
    @staticmethod
    def get_product_from_cache():
        """Получает данные по продуктам из кэша. Если кэш пуст, получает данные из БД"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "product_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products, 60)
        return products

    @staticmethod
    def get_products_from_category(category_id: int):
        """Отдаёт данные по продуктам из заданной категории"""
        return Product.objects.filter(category_id=category_id)
