from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Comment
from .models import Report


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Report)
