from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

def welcome_view(request):
    return HttpResponse("<h1>hello world</h1>")

def register_view(request):
    ctx = {}
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx['form'] = form
    return render(request, "register.html", ctx)

def login_view(request):
    ctx = {}
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx['form'] = form
    return render(request, "login.html", ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))