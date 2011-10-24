from settings.base import *

import json
with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hello',
        'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),
    }
}

MEDIA_ROOT = '/home/dotcloud/data/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/dotcloud/data/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = 'secret key'
