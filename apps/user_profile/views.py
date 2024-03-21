from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# views.py
from apps.all_posts.models import Article, Comment, Report


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }
    return render(request, 'user_profile/profile.html', context)


@login_required
def submissions(request, username):
    user = get_object_or_404(User, username=username)

    articles = Article.objects.filter(created_by=user)
    safe_articles = []
    red_articles = []
    for article in articles:
        if article.number_of_report >= settings.MIN_SAFE_REPORTS:
            red_articles.append(article)
        else:
            safe_articles.append(article)

    context = {
        'user': user,
        'articles': articles,
        'safe_articles': safe_articles,
        'red_articles': red_articles,
    }

    return render(request, 'user_profile/submissions.html', context)


@login_required
def comments(request, username):
    user = get_object_or_404(User, username=username)
    comments = Comment.objects.filter(created_by=user).order_by('-created_at')

    context = {
        'comments': comments,
        'user': user,
    }

    return render(request, 'user_profile/comments.html', context)
