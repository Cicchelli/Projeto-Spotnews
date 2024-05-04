from django.shortcuts import render, get_object_or_404, redirect
from news.models import Category, News, User
from news.forms import CreateCategoriesForm, NewsForm


def index(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news_details = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news_details": news_details})


def categories_form(request):
    form = CreateCategoriesForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Category.objects.create(**form.cleaned_data)
        return redirect("home-page")
    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    users = User.objects.all()
    categories = Category.objects.all()
    form = NewsForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home-page")

    return render(
        request,
        "news_form.html",
        {"form": form, "users": users, "categories": categories},
    )
