from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed


# Create your views here.

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("frontpage")
    else:
        form = RegisterForm() 
    return render(response, "register/register.html", {"form":form})

def logout_user(request):
    print("logout_test")
    logout(request)
    return redirect("frontpage")
    