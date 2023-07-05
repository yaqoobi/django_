from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "registration/index.html")


def login(request):
    return render(request, "registration/login.html")


def register(request):
    return render(request, "registration/register.html")


def logout(request):
    return render(request, "registration/logout.html")
