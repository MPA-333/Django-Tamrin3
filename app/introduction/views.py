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


def museumView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/museum.html", context)


def gardenView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/garden.html", context)


def visit_wayView(request):
    context = {
        "load_media": settings.MEDIA_URL
    }
    return render(request, "introduction/visit_way.html", context)
