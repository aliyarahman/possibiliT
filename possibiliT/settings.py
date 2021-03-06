"""
Django settings for gaytabase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import psycopg2
import urlparse
from urlparse import urlparse
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j!h0x=i!_)_d52pwbrzhou+6e&c4r4^7+7zayqc(0=kzo#%cp+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'possibiliT.urls'

WSGI_APPLICATION = 'possibiliT.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '' # This is where you want the collectstatic app to put all of the files for deployment, when it pulls from multiple DIRS
STATIC_URL = '/static/' #This is the part that comes before what you are using in {% static %} tags to reference files
STATIC_DIRS = '/home/aliya/gitrepos/possibiliT/app/static/app/' #These are where the files are actually stored - this is really important for deployment on servers like Bluehost where you can't save inside your project directory


TEMPLATE_DIRS = (
	'/home/aliya/gitrepos/possibiliT/app/templates/app/',
	'app/templates/app/',
)

LOGIN_URL = 'login_view'
LOGIN_REDIRECT_URL = 'index'

AUTH_USER_MODEL = 'auth.User'
