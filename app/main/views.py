from django.shortcuts import render

def homeView(request):
    return render(request, "main/home.html")
