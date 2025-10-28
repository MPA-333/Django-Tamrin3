from django.urls import path
from app.main.views import homeView

urlpatterns = [
    path("", homeView, name="home"),
]
