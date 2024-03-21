from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Report
from django.db.models import Count
from django.db import models

import datetime


# Create your views here.


def frontpage(request):

    articles = Article.objects.exclude(
        id__in=Report.objects.values('article').annotate(report_count=Count('article')).filter(
            report_count__gte=2).values('article')
    ).order_by('-created_at')[0:100]
    if request.user.is_authenticated:
        for article in articles:
            article.has_reported = False
            if Report.objects.filter(reported_by=request.user, article=article).first():
                article.has_reported = True
    context = {
        'articles': articles,
    }
    return render(request, 'all_posts/frontpage.html', context)


def get_comment_dict(comment):
    return {
        'id': comment.id,
        'created_by': comment.created_by.id,
        'username': comment.created_by.username,
        'text': comment.content,
        'pubDate': comment.created_at,
        'child_comments': [get_comment_dict(child) for child in
                           comment.comment_set.select_related('created_by').all().order_by('-created_at')]
    }


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.select_related('created_by').filter(article=article,
                                                                   parent_comment__isnull=True).order_by('-created_at')
    comments_dict = [get_comment_dict(comment) for comment in comments]
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
        print(comments_dict)

    context = {
        'article': article,
        'form': form,
        'comments_dict': comments_dict
    }
    return render(request, 'all_posts/details.html',context )


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
    context = {
        'form': form
    }
    return render(request, 'all_posts/submit.html', context)


@login_required
def report(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    # next_page = request.GET.get('next_page', '')

    if article.created_by != request.user and not Report.objects.filter(reported_by=request.user, article=article):
        report = Report.objects.create(article=article, reported_by=request.user)
        return redirect('frontpage')
    # if next_page == 'get_article':
    #     return redirect('get_article', article=article_id)
    else:
        return redirect('frontpage')

@login_required
def unreport(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    existing_report = Report.objects.filter(reported_by=request.user, article=article).first()

    if existing_report:
        # If the user has reported the article, delete the report
        existing_report.delete()
        return redirect('frontpage')

    # Redirect the user to the front page or any other appropriate page
    return redirect('frontpage')
