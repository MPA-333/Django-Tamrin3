from django.urls import path
from app.article.views import MainView

urlpatterns = [
    path("main/", MainView.as_view(), name="e_home"),
]