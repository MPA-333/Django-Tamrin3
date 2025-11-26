from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from app.article.models import Article


class MainView(TemplateView):
    template_name = "article/main.html"

class ArticleView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "article/article_list.html"

