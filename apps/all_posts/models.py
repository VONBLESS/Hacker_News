from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Article(models.Model):

    title = models.CharField(max_length=255)
    url = models.URLField()

    flags = models.IntegerField(default=0)

    # content = models.TextField()
    
    created_by= models.ForeignKey(User, related_name="artiles",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    article = models.ForeignKey(Article, related_name='comments',on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        if self.parent_comment:
            return f"Comment by {self.created_by.username} on  '{self.parent_comment}'"
        else:
            return f"Comment by {self.created_by.username} on article '{self.article.title}'"    
    @property
    def is_reply(self):
        return self.parent_comment is not None


