import os

from simpletodo.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('SIMPLETODO_DB_NAME'),
    },
}

ROLLBAR = {
    'access_token': os.getenv('SIMPLETODO_ROLLBAR_TOKEN'),
    'environment': 'development',
    'branch': 'master',
    'root': '/absolute/path/to/code/root',
}
