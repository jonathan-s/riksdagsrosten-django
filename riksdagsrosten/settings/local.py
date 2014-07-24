from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# type of database
# user (jonathan) : password
# localhost
# port
# name of database connection riksdagsrosten

DATABASES = { 'default': dj_database_url.config(
        default="postgres://jonathan@localhost:5432/riksdagsrosten")}

ALLOWED_HOSTS = ['*']

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

THIRD_PARTY = (
    'debug_toolbar',
    'django_nose',
    #'debug_toolbar.apps.DebugToolbarConfig', this one is for Django 1.7
)

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY