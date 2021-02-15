import os

from simpletodo.settings.common import *

DEBUG = True

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
    'root': BASE_DIR,
}
