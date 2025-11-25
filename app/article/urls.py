from django.urls import path
from app.article.views import MainView, ArticleView

urlpatterns = [
    path("main/", MainView.as_view(), name="e_home"),
    path("main/articles/", ArticleView.as_view(), name="articles"),
]