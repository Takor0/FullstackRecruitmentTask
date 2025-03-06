from django.core.management.base import BaseCommand
from djangotask.models import AppUser, Discussion, Comment
from django.db.models import Count


class Command(BaseCommand):
    help = "Print queries"

    def handle(self, *args, **options):
        print(AppUser.objects.exclude(email=""))
        print(
            Discussion.objects.annotate(comment_count=Count("comments")).filter(
                comment_count__gt=10
            )
        )
        print(Comment.objects.exclude(app_user__metadata={}))
