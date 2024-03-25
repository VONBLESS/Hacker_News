"""
URL configuration for MyNews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from apps.base import views as base_views
from apps.all_posts import views as all_posts_views
from apps.user_profile import views as user_profile_views
import MyNews.settings as settings

urlpatterns = [

    path('', include("django.contrib.auth.urls")),
    # path('/login')
    path('admin/', admin.site.urls),
    path("ur/<int:article_id>",all_posts_views.unreport, name="unreport"),
    path("r/<int:article_id>", all_posts_views.report, name="report"),
    path("home/", all_posts_views.frontpage, name="home"),
    path("register/", base_views.register, name='register'),
    path('login/', base_views.user_login, name='login'),
    path("logout/", base_views.logout_user, name="logout"),
    path("", all_posts_views.frontpage, name="frontpage"),
    path('submit/', all_posts_views.submit, name="submit"),
    path('a/<int:article_id>/', all_posts_views.get_article, name="get_article"),
    path('u/<str:username>/', user_profile_views.user_profile, name='my_profile'),
    path('u/<str:username>/submissions', user_profile_views.submissions, name='my_submissions'),
    path('u/<str:username>/comments', user_profile_views.comments, name="my_comments"),
    path("__debug__/", include("debug_toolbar.urls")),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns