from django.db import models


class AppUser(
    models.Model
):  # CHANGE: User -> AppUser to avoid conflict with Django's User model
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True)
    metadata = models.JSONField(blank=True, default=dict)  # CHANGE: {} -> dict


class Discussion(models.Model):
    title = models.CharField(max_length=100)


class Comment(models.Model):
    content = models.TextField()
    app_user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="comments"
    )
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="comments"
    )
