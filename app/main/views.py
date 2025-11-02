from django.shortcuts import render
from app.introduction.models import Message
from app.main.forms import MessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings

def homeView(request):
    return render(request, "main/home.html")


def aboutView(request):
    context = {}
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message()
            message.code = 7
            message.name = data["name"]
            message.family = data["family"]
            message.email = data["email"]
            message.subject = data["subject"]
            message.text = data["text"]
            message.save()
            return HttpResponseRedirect(reverse_lazy("home"))
    else:
        form = MessageForm()
        
    context["form"] = form
    context["load_media"] = settings.MEDIA_URL
    return render(request, "main/about.html", context)
