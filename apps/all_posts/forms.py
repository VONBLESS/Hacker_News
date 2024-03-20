from django import forms
from .models import Article, Comment

from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','url',)
        # fields = ('title', 'url', 'content')
        widgets = {
            'title': forms.Textarea(attrs={
                'rows': '1',
                'cols': '90',
                'maxlength': '100',
            }),
            'url': forms.Textarea(attrs={
                'rows': '1',
                'cols': '90',
                'maxlength': '100',
            }),
        }
class CommentForm(forms.ModelForm):
    # parent_comment_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': '5',
                'cols': '90',
                'maxlength': '100',
            }),
        }



    