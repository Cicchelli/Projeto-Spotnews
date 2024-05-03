from django.db import models
from news.validators import validate_category_name


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_category_name]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name
