from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "registration/login.html")


def register(request):
    return render(request, "registration/register.html")
