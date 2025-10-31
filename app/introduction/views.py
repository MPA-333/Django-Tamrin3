from django.shortcuts import render
from django.conf import settings


def introView(request):
    return render(request, "introduction/intro.html")


def historyView(request):
    return render(request, "introduction/history.html")


def departmentView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/department.html", context)
