from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# type of database
# user (jonathan) : password
# localhost
# port
# name of database connection riksdagsrosten

BROKER_URL = "amqp://jonathan:password@localhost:5672/myvhost"
CELERY_ALWAYS_EAGER = True

DATABASES = { 'default': dj_database_url.config(
        default="postgres://jonathan@localhost:5432/riksdagsrosten")}

ALLOWED_HOSTS = ['*']

TEST_RUNNER = 'riksdagsrosten.test_runner.CeleryTestWithNoseRunner'

NOSE_ARGS = ['--nologcapture']

THIRD_PARTY = (
    'debug_toolbar',
    'django_nose',
    'livereload'
    #'debug_toolbar.apps.DebugToolbarConfig', this one is for Django 1.7
)

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY