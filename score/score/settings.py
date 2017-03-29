"""
Django settings for score project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-8%7qr#sipf=w&ce2=g81=!og_5ohpns*r&fy%r7)m7=5-rf7z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = '1'
# Application definition
'''
AUTHENTICATION_BACKENDS = (
    'score.auth_backend.CustomUserModelBackend',
)


CUSTOM_USER_MODEL = 'blog.ExtendedUser'
'''

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles','ajaximage',
    'django_wysiwyg','django.contrib.comments',
    'ckeditor','blog','connections',
)







CKEDITOR_UPLOAD_PATH = "uploads/"

DJANGO_WYSIWYG_FLAVOR = "ckeditor"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
   # 'score.middleware.Auth',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'score.urls'

WSGI_APPLICATION = 'score.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tem',
        'USER': 'amit',
        'PASSWORD': 'amitt',
        'HOST': '',
        'PORT': '',

    }
}

LOGIN_URL = '/login/'

TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth',
    'blog.context_processors.userdetails',)

TEMPLATE_DIRS = (
'/home/amitt/proj/score/templates/',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

MEDIA_URL = '/media/'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
STATICFILES_DIRS = ( '/home/amitt/proj/score/static/', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home/amitt/proj/score/'

STATIC_URL = '/static/'

MEDIA_ROOT = '/home/amitt/proj/score/media/'

#AJAXIMAGE_DIR = 'ajaximage/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
