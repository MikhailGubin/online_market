from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории товаров",
        help_text="Введите наименование категории товаров",
    )
    description = models.TextField(
        verbose_name="Описание категории товаров",
        help_text="Введите категории товаров",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория товаров"
        verbose_name_plural = "категории товаров"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    product_image = models.ImageField(
        upload_to="product/images",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Стоимость продукта",
        help_text="Введите стоимость продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации продукта",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения информации о продукте",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        default=0,
        blank=True,
    )
    can_unpublish_product = models.BooleanField(
        default=False,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} из категории {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
            "category",
            "price",
            "created_at",
            "updated_at",
            "views_counter",
        ]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_any_product", "Can delete any product"),
        ]
