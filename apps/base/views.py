from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# from django.http import HttpResponseNotAllowed

# Create your views here.

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.register()
            return redirect("frontpage")
    else:
        form = RegisterForm()
    print("hi")
    context = {
        "form": form,
    }
    return render(response, "register/register.html", context)


def logout_user(request):
    print("logout_test")
    logout(request)
    return redirect("frontpage")


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            hashed_password = make_password(password)
            # print("CHECKING", check_password(password, hashed_password))
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Successful login
                if "next" in request.POST:

                    next_url = request.GET.get("next")
                    if "username_placeholder" in next_url:
                        # Replace 'username_placeholder' with the actual username
                        next_url = next_url.replace(
                            "username_placeholder", str(request.user.username)
                        )
                    return redirect(next_url)
                else:
                    return redirect(
                        "frontpage"
                    )  # Adjust 'frontpage' to your actual homepage URL name
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login/login.html", {"form": form})
