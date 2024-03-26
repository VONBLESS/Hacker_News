from django.urls import path

from . import views


app_name = "user_profile"
urlpatterns = [
    path("u/<str:username>/", views.user_profile, name="my_profile"),
    path("u/<str:username>/submissions", views.submissions, name="my_submissions"),
    path("u/<str:username>/comments", views.comments, name="my_comments"),
]
