from django.shortcuts import render
from django.views import *
from django import views

# Create your views here.


def home(request):
    return render(request, "html/index.html")
