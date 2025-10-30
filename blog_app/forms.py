from django import forms

from blog_app.models import Blog
from constants import FORBIDDEN_WORDS
from mixin_form import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Blog
        exclude = ("views_counter",)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title:
            if any(word in title.lower() for word in FORBIDDEN_WORDS):
                self.add_error("title", "Название блога содержит запрещённое слово")
            if content:
                if any(word in content.lower() for word in FORBIDDEN_WORDS):
                    self.add_error(
                        "content", "В содержании блога присутствует запрещённое слово"
                    )
