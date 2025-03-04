from django.core.management.base import BaseCommand
from models.models import User, Discussion, Comment

class Command(BaseCommand):
    help = 'Seed database with basic data'

    def handle(self, *args, **options):
        # Create a user
        user, created = User.objects.get_or_create(
            username='bob',
            defaults={'email': 'bob@example.com', 'metadata': {'bio': 'Enthusiastic learner'}}
        )

        # Create a discussion
        discussion, created = Discussion.objects.get_or_create(
            title='Django Best Practices'
        )
        discussion, created = Discussion.objects.get_or_create(
            title='Should have 3 comments'
        )

        # Create a comment
        for i in range(3):
            comment, created = Comment.objects.get_or_create(
                content=f'I belong to should have {i}!',
                user=user,
                discussion=discussion
            )



        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
