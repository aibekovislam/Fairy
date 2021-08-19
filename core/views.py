from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404

def main(request):
    if request.user.is_authenticated:
        publics = Publics.objects.all()
        publics = Publics.objects.order_by('-date')
        return render(request, "main.html", {"publics": publics})
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
        return render(request, "index.html")

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

def add_like(request, pk):
    try:
        if request.user.is_authenticated:
            public = Publics.objects.get(pk=pk)
            public.likes += 1 
            public.save()
    except:
        return redirect(register)
    return redirect(main)

def add_dislike(request, pk):
    try:
        if request.user.is_authenticated:
            public = Publics.objects.get(pk=pk)
            public.dislikes += 1
            public.save()
    except ObjectDoesNotExist:
        return Http404
    return redirect(main)


def publish(request):
    if request.method == 'GET':
        return render(request, "publish.html")
    elif request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        image = request.FILES.get("image")
        new_publish = Publics(title=title, text=text, image=image)
        new_publish.save()
        user = request.user


        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nik=user.username)
            author.save()

        author = user.author
        new_publish.author = author
        new_publish.save()
        return redirect (main)


def author(request, pk):
    author = Author.objects.get(pk=pk)
    context={
        "author": author,
        "user": author.user
    }
    return render(request, "author_page.html", context)


def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html", {"authors": authors})

def delete_publics(request, pk):
    public = Publics.objects.get(pk=pk)
    public.delete()
    return redirect(main)


def comments(request, pk):
    comment = Comments.objects.get(pk=pk)
    context={
        "comment": comment,
        "user": author.user
    }
    return render(request, context, "comments.html")