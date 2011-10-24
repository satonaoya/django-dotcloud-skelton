import os
from settings.base import *

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite.db'),
    }
}

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')
STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = '/static/grappelli/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
      os.path.join(PROJECT_ROOT, 'templates'),
)


INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

LOGIN_REDIRECT_URL = '/'
