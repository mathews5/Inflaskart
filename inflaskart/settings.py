#-*- coding: UTF-8 -*-
"""
Django settings for inflaskart project.
Generated by 'django-admin startproject' using Django 1.10.3.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
For deployment on Heroku, see
https://devcenter.heroku.com/articles/django-app-configuration
"""

import os
import dj_database_url


# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# updated for deployment on Heroku
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'grocerystore.apps.GrocerystoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # django.contrib.staticfiles collects the static files from each of your
    # applications into STATIC_ROOT (that can easily be served in production)
    'django.contrib.staticfiles',
    'favicon',
    'storages',
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


ROOT_URLCONF = 'inflaskart.urls'


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
            ],
        },
    },
]


WSGI_APPLICATION = 'inflaskart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'grocerystore_db',
        # the following settings aren't used with sqlite3:
        'USER': 'EGlelek',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(PROJECT_ROOT, 'secret_key.txt')) as f:
        SECRET_KEY = f.read().strip()
except:
    SECRET_KEY = os.environ['SECRET_KEY']


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# NotaBene: https://docs.djangoproject.com/en/1.10/howto/static-files/
# absolute path to the directory where collectstatic will collect static files for deployment
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]


# default Django backend storage was: 'django.core.files.storage.FileSystemStorage'
# setting media file storage on Amazon S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'inflaskart'
# before using AMazon S3 server: MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_ROOT = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = os.path.join(MEDIA_ROOT, 'media/')
MEDIA_URL = 'https://inflaskart.herokuapp.com/media/'

try:
    with open(os.path.join(PROJECT_ROOT, 'aws_access_key_id.txt')) as f:
        AWS_ACCESS_KEY_ID = f.read().strip()
except:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

try:
    with open(os.path.join(PROJECT_ROOT, 'aws_secret_access_key.txt')) as f:
        AWS_SECRET_ACCESS_KEY = f.read().strip()
except:
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

#Simplified static file serving. https://warehouse.python.org/project/whitenoise/
#Enabling gzip functionality
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
