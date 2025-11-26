from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from app.article.models import Article, Author


class MainView(TemplateView):
    template_name = "article/main.html"

class ArticleView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "article/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["load_media"] = settings.MEDIA_URL
        return context
    

