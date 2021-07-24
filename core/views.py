from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def main(request):
    publics = Publics.objects.all()
    return render(request, "main.html", {"publics": publics})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return  render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        
        return redirect(main)


def sign_out(request):
    logout(request)
    return redirect(sign_in)