import os
import sys
sys.path = sys.path + ["/home/dotcloud/current/hello/"]
os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings.production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
