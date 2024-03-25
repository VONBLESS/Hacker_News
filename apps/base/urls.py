from django.urls import path

from . import views


app_name = "base"
urlpatterns = [
    path("register/", views.register, name='register'),
    path("logout/", views.logout_user, name="logout"),
]
