# from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "alou/index.html")


def padilha(request):
    return HttpResponse("Hello Padilha")


def greet(request, name):
    return render(request, "alou/greet.html", {
        "name": name.capitalize()
    })