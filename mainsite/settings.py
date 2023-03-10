"""
Django settings for mainsite project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import sys

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(#8%x+ef7t)5y(hr$_-w1robiesir601yq)j5(w2spdc_697ug'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'video_tasks',
    # 'django_rq',  # optional (not needed when using TaskThreaded)
    'django_task',
    'django_task_example_02',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mainsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mainsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# set for models.ImafeField to work
MEDIA_URL = '/fieldfiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'fieldfiles')


# ##############################################################################
#   Echo helpers

def settings_echo(message, title='', error=False, warning=False):
    """
    Helpers to display a message
    """
    # Avoid echoing twice when executing runserver
    if os.environ.get('RUN_MAIN') is None:
        if error:
            prefix = "\x1b[41;37m"
        elif warning:
            prefix = "\x1b[43;30m"
        else:
            prefix = "\x1b[47;30m"
        suffix = " \x1b[0m"
        if title:
            print(prefix + str(title) + ':' + suffix, file=sys.stderr, end ="")
        print(prefix + str(message) + suffix, file=sys.stderr,)

# ##############################################################################
INSTANCE_PREFIX = "example"

SESSION_COOKIE_NAME = INSTANCE_PREFIX + '_sid'

settings_echo(INSTANCE_PREFIX, title='INSTANCE_PREFIX')
settings_echo(SESSION_COOKIE_NAME, title='SESSION_COOKIE_NAME')

### celery settings ###
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
###

#
# Redis config
#

#REDIS_URL = 'redis://localhost:6379/0'
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = 6379
REDIS_URL = 'redis://%s:%d/0' % (redis_host, redis_port)
settings_echo(REDIS_URL, title='REDIS_URL')


RQ_SHOW_ADMIN_LINK = False
DJANGOTASK_LOG_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'protected', 'tasklog'))
DJANGOTASK_ALWAYS_EAGER = False
DJANGOTASK_JOB_TRACE_ENABLED = False
DJANGOTASK_REJECT_IF_NO_WORKER_ACTIVE_FOR_QUEUE = True

QUEUE_DEFAULT = INSTANCE_PREFIX + '_default'
QUEUE_LOW = INSTANCE_PREFIX + '_low'
QUEUE_HIGH = INSTANCE_PREFIX + '_high'

RQ_QUEUES = {
    QUEUE_DEFAULT: {
        'URL': REDIS_URL,
        #'PASSWORD': 'some-password',
        #'DEFAULT_TIMEOUT': 5 * 60,
        'DEFAULT_TIMEOUT': -1,  # -1 means infinite
    },
    QUEUE_LOW: {
        'URL': REDIS_URL,
        #'ASYNC': False,
        'DEFAULT_TIMEOUT': 10 * 60,
    },
    QUEUE_HIGH: {
        'URL': REDIS_URL,
        'DEFAULT_TIMEOUT': 500,
    },
}

