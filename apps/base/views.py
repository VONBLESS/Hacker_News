from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
import logging

# from django.http import HttpResponseNotAllowed

# Create your views here.

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("frontpage")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(response, "register/register.html", context)


def logout_user(request):
    print("logout_test")
    logout(request)
    return redirect("frontpage")


logger = logging.getLogger(__name__)
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Successful login
                if "next" in request.POST:

                    next_url = request.GET.get('next')
                    print("Original next URL:", next_url)
                    if 'username_placeholder' in next_url:
                        # Replace 'username_placeholder' with the actual username
                        next_url = next_url.replace('username_placeholder', str(username))
                    print("Next URL:", next_url)
                    return redirect(next_url)
                else:
                    return redirect('frontpage')  # Adjust 'frontpage' to your actual homepage URL name
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

