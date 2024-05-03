from django.urls import path
from news.views import index


urlpatterns = [
    path("http://127.0.0.1:8000", index, name="home-page"),
]
