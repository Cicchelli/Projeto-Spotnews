from django.shortcuts import render, get_object_or_404, redirect
from news.models import Category, News
from news.forms import CreateCategoriesForm


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
