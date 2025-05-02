import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Загружает тестовые продукты в базу данных из фикстуры'

    def handle(self, *args, **kwargs):

        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from category_fixture.json'))

        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from product_fixture.json'))

        # category_1, _ = Category.objects.get_or_create(
        #     name='Смартфоны',
        #     description="Смартфоны, как средство не только коммуникации, "
        #                 "но и получение дополнительных функций для удобства жизни",
        # )
        # category_2, _ = Category.objects.get_or_create(
        #     name='Телевизоры',
        #     description="Современный телевизор, который позволяет наслаждаться просмотром,"
        #                 " станет вашим другом и помощником",
        # )
        #
        # products = [
        #     {
        #         "name": "Iphone 15",
        #         "description": "512GB, Черный цвет, 48+12MP камера",
        #         "product_image": os.path.join(BASE_DIR, 'static/images/iphone_15.jpg'),
        #         "category": category_1,
        #         "price": 120000.0,
        #     },
        #     {
        #         "name": "Samsung Galaxy S23 Ultra",
        #         "description": "256GB, Серый цвет, 200MP камера",
        #         "product_image": os.path.join(BASE_DIR, 'static/images/galaxy_s23.jpg'),
        #         "category": category_1,
        #         "price": 96999.0,
        #     },
        #     {
        #         "name": "Samsung QE65QN85DBUXRU",
        #         "description": "Диагональ 65\", разрешение экрана 4K UltraHD, 3840x2160",
        #         "product_image": "",
        #         "category": category_2,
        #         "price": 135999.0,
        #     },
        # ]
        #
        # for product_data in products:
        #     product, created = Product.objects.get_or_create(**product_data)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))
