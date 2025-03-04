import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'replace-this-with-a-secure-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.contenttypes',  # Required for Django models
    'django.contrib.auth',          # Required for user authentication and models
    'models',                       # Our custom app containing source 1 (models)
]

MIDDLEWARE = []

ROOT_URLCONF = 'django_task.urls'

TEMPLATES = []

WSGI_APPLICATION = 'django_task.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
