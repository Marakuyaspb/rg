import os, sys
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
   'https://rgauto.pro',
   'https://www.rgauto.pro',
]

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }

}

ADMINS = [
    ('Annaa', 'info@rgspace.pro'),
]