from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from constants import FORBIDDEN_WORDS
from mixin_form import StyleFormMixin


def validate_price(value):
    if value < 0:
        raise ValidationError("Цена продукта не может быть отрицательной")


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            if any(word in name.lower() for word in FORBIDDEN_WORDS):
                self.add_error("name", "Название товара содержит запрещённое слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            if any(word in description.lower() for word in FORBIDDEN_WORDS):
                self.add_error(
                    "description", "Описание товара содержит запрещённое слово"
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        validate_price(price)
        return price


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Product
        fields = ("name", "can_unpublish_product",)
