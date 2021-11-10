from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy



# Create your views here.


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def signup(request):
    return render(request, "main/signup.html")

def signin(request):
        return render(request, 'main/signin.html')

def logintutor(request):
    return render(request, "main/loginpagetutor.html")

def loginstu(request):
    return render(request, "main/loginpagestud.html")

def studentsignup(request):
    return render(request, "main/studentsignup.html")

def tutorsignup(request):
    return render(request, "main/tutorsignup.html")

def list(request):
    return render(request, "main/list.html")

def register(request):
        return render(request, '../templates/users/register.html')

