from django.urls import path
from app.main.views import homeView, aboutView

urlpatterns = [
    path("", homeView, name="home"),
    path("about/", aboutView, name="about"),
]
