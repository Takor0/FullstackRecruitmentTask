import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        INSTALLED_APPS=[
            'models',  # replace with your app name
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # or a specific database file
            }
        },
        # Add other required settings as needed
    )

django.setup()

# Now you can import and use your models.
from python.django_task.models.models import Discussion

# Example usage:
print(Discussion.objects.all())
