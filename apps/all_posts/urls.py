from django.urls import path

from . import views


app_name = "all_posts"

urlpatterns = [
    path("ur/<int:article_id>", views.unreport, name="unreport"),
    path("r/<int:article_id>", views.report, name="report"),
    path("home/", views.frontpage, name="home"),

    path("", views.frontpage, name="frontpage"),
    path('submit/', views.submit, name="submit"),
    path('a/<int:article_id>/', views.get_article, name="get_article"),
]