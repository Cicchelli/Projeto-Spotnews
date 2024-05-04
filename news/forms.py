from django import forms
from news.models import News


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(max_length=200)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
