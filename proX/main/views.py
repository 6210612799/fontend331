from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def signup(request):
    return render(request, "main/signup.html")

def signin(request):
    return render(request, "main/signin.html")

def logintutor(request):
    return render(request, "main/loginpagetutor.html")

def loginstu(request):
    return render(request, "main/loginpagestud.html")