from django.db import models
from apps.base.models import CustomUser


# Create your models here.
# from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    number_of_report = models.IntegerField(default=0)

    # content = models.TextField()

    created_by = models.ForeignKey(
        CustomUser, related_name="articles", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Report(models.Model):
    article = models.ForeignKey(
        Article, related_name="reports", on_delete=models.CASCADE
    )

    reported_by = models.ForeignKey(
        CustomUser, related_name="reports", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.article.number_of_report += 1
        self.article.save()

        super(Report, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.article.number_of_report -= 1
        self.article.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.article} with {self.article.number_of_report} Reports"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
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
