from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True)
    metadata = models.JSONField(blank=True, default={})


class Discussion(models.Model):
    title = models.CharField(max_length=100)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="comments"
    )
