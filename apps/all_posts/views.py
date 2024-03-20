from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
import datetime

# Create your views here.
def frontpage(request):
    articles = Article.objects.all().order_by('-created_at')[0:100]
    return render(request,'all_posts/frontpage.html', {'articles':articles})


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #  
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')
            parent_comment = None
            if parent_comment_id:
                parent_comment = Comment.objects.get(pk=parent_comment_id)
            comment = form.save(commit=False)
            comment.article = article
            comment.created_by = request.user
            comment.parent_comment = parent_comment
            comment.save()
            return redirect('get_article', article_id=article_id)
    else:
        form = CommentForm()
    return render(request,'all_posts/details.html',{'article': article, 'form':form})

        
@login_required
def submit(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()

            return redirect('frontpage')
    else:
        form = ArticleForm()
    return render(request, 'all_posts/submit.html',{'form':form})

# @login_required
