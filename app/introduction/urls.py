from django.urls import path
from app.introduction.views import introView, historyView, departmentView, museumView, gardenView, visit_wayView

urlpatterns = [
    path("", introView, name="intro"),
    path("history/", historyView, name="history"),
    path("department/", departmentView, name="department"),
    path("department/museum/", museumView, name="museum"),
    path("department/garden/", gardenView, name="garden"),
    path("visit-way", visit_wayView, name="way"),
]
