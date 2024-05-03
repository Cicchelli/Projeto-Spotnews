from django.urls import path
from news.views import index, news_details


urlpatterns = [
    path("http://127.0.0.1:8000", index, name="home-page"),
    path(
        "http://127.0.0.1:8000/news/<int:id>",
        news_details,
        name="news-details-page",
    ),
]
