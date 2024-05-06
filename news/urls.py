from django.urls import path, include
from rest_framework import routers
from news.views import (
    CategoryViewSet,
    index,
    news_details,
    categories_form,
    news_form,
    UserViewSet,
    NewsViewSet,
)

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)
router.register(r"news", NewsViewSet)

urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", news_form, name="news-form"),
    path("api/", include(router.urls)),
]
