from django.core.management.base import BaseCommand
from djangotask.models import AppUser, Discussion, Comment


class Command(BaseCommand):
    help = "Create fixtures to test queries"

    def handle(self, *args, **options):
        app_users = []
        for user_data in [
            {"username": "test_user_1", "email": ""},
            {"username": "test_user_2", "email": "user@mail.com"},
            {"username": "test_user_3", "email": "", "metadata": {"age": 32}},
        ]:
            app_user, _ = AppUser.objects.get_or_create(**user_data)
            app_users.append(app_user)

        discussion, created = Discussion.objects.get_or_create(
            title="To be or not to be?"
        )

        for i in range(5):
            Comment.objects.get_or_create(
                content=f"This is comment NO: {i}!",
                app_user=app_users[2],
                discussion=discussion,
            )

        discussion_2, _ = Discussion.objects.get_or_create(title="be!")

        for i in range(11):
            Comment.objects.get_or_create(
                content=f"This is comment 2.0 NO: {i}!",
                app_user=app_users[0],
                discussion=discussion_2,
            )

        self.stdout.write(self.style.SUCCESS("Added fixtures"))
