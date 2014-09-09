from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
from riksdagsrosten.settings.base import get_env_variable

SETTINGS_MODULE = 'DJANGO_SETTINGS_MODULE'
os.environ.setdefault(SETTINGS_MODULE,
    get_env_variable(SETTINGS_MODULE, 'riksdagsrosten.settings.base'))

app = Celery('riksdagsrosten')

app.config_from_object(
    get_env_variable(SETTINGS_MODULE, 'riksdagsrosten.settings.base'))
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()