from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название блога",
        help_text="Введите название блога",
    )
    content = models.TextField(
        verbose_name="Содержание блога",
        help_text="Введите содержание блога",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="blog_app/images",
        blank=True,
        null=True,
        verbose_name="Изображение для блога",
        help_text="Загрузите изображение для блога",
    )
    publication_sign = models.BooleanField(
        default=False,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания блога",
    )
    views_number = models.IntegerField(
        verbose_name="Количество просмотров",
        default=0,
        blank=True,
    )

    def __str__(self):
        return f"Название блога '{self.title}'"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title", "publication_sign", "created_at", "views_number"]
