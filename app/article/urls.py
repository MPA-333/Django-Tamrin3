from django.urls import path
from app.article.views import (
    MainView,
    ArticleView,
    ArticleDetailView,
    downloadArticleView,
)

urlpatterns = [
    path("main/", MainView.as_view(), name="e_home"),
    path("main/articles/", ArticleView.as_view(), name="articles"),
    path("main/article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path(
        "main/article/download_pdf/<int:pk>", downloadArticleView, name="download_pdf"
    ),
]
