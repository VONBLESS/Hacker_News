from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# views.py
from apps.all_posts.models import Article, Comment


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile/profile.html', {'user': user})
@login_required
def submissions(request, username):
    user = get_object_or_404(User, username=username)

    articles = Article.objects.filter(created_by=user)

    return render(request, 'user_profile/submissions.html', {'articles': articles, 'user': user})
@login_required
def comments(request, username):
    user = get_object_or_404(User, username=username)
    comments = Comment.objects.filter(created_by=user).order_by('-created_at')

    return render(request, 'user_profile/comments.html', {'comments': comments, 'user': user})
