import os

from split_settings.tools import include

include(
    'common.py',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Django database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('SIMPLETODO_DB_NAME'),
        'USER': os.getenv('SIMPLETODO_DB_USER'),
        'PASSWORD': os.getenv('SIMPLETODO_DB_PASS'),
        'HOST': os.getenv('SIMPLETODO_DB_HOST'),
        'PORT': os.getenv('SIMPLETODO_DB_PORT'),
    },
}
