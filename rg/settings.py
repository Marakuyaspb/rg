import os, sys
from pathlib import Path
from django.contrib.messages import constants as messages
from celery import Celery
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))

DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
   'https://rgauto.pro',
   'https://www.rgauto.pro',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'cars.apps.CarsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'rg.context_processors.page_title',
            ],
        },
    },
]

WSGI_APPLICATION = 'rg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.environ.get("DB_NAME"),
    #     'USER': os.environ.get("DB_USER"),
    #     'PASSWORD': os.environ.get("DB_PASSWORD"),
    #     'HOST': os.environ.get("DB_HOST"),
    #     'PORT': os.environ.get("DB_PORT"),
    # }

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# for prod
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CELERY
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'


EMAIL_DEBUG = True


#SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.timeweb.ru'  
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_HOST_USER = str(os.getenv('TW_MAIL'))
EMAIL_HOST_PASSWORD = str(os.getenv('TW_PASSWORD'))