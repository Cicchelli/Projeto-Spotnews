from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200, validators=[news.models.validate_title]
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateField()),
                (
                    "img",
                    models.ImageField(blank=True, null=True, upload_to="img/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.user",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="news", to="news.category"
                    ),
                ),
            ],
        ),
    ]
