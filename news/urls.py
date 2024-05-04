from django.urls import path

from news.views import index, news_details, categories_form, news_form


urlpatterns = [
    path("http://127.0.0.1:8000", index, name="home-page"),
    path(
        "http://127.0.0.1:8000/news/<int:id>",
        news_details,
        name="news-details-page",
    ),
    path(
        "http://127.0.0.1:8000/categories/",
        categories_form,
        name="categories-form",
    ),
    path("http://127.0.0.1:8000/news/", news_form, name="news-form"),
]
