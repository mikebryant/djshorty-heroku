import dj_database_url
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}

DEBUG = True

INSTALLED_APPS = [
    'shorty',
]

LOGIN_URL = 'admin:login'

LOGOUT_URL = 'admin:logout'

ROOT_URLCONF = 'django_autoconfig.autourlconf'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
