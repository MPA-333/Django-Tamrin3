from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app.article.models import Article


# ====================================================
# ====================================================
class MainView(TemplateView):
    template_name = "article/main.html"


# ====================================================
# ====================================================
class ArticleView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "article/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["load_media"] = settings.MEDIA_URL
        return context


# ====================================================
# ====================================================
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article_detail"
    template_name = "article/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["load_media"] = settings.MEDIA_URL
        return context


# ====================================================
# ====================================================
def downloadArticleView(request, pk):
    article = Article.objects.get(id=pk)
    fss = FileSystemStorage()
    fileName = article.article.name
    if fss.exists(fileName):
        with fss.open(fileName) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = "attachment; filename=Article.pdf"
            return response
    else:
        return HttpResponseNotFound("فایل مورد نظر یافت نشد")


# ====================================================
# ====================================================
