from __future__ import absolute_import, unicode_literals

from django.conf import settings
try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as DiscoverRunner

from celery import current_app
from django_nose import NoseTestSuiteRunner

USAGE = """\
Custom test runner to allow testing of celery delayed tasks.
"""


def _set_eager():
    settings.CELERY_ALWAYS_EAGER = True
    current_app.conf.CELERY_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True  # Issue #75
    current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

class CeleryTestWithNoseRunner(NoseTestSuiteRunner):
    """Custom defined class to run test with nose and Celery"""
    def setup_test_environment(self, **kwargs):
        _set_eager()
        super().setup_test_environment(**kwargs)

class CeleryTestSuiteRunner(DiscoverRunner):
    """Django test runner allowing testing of celery delayed tasks.
    All tasks are run locally, not in a worker.
    To use this runner set ``settings.TEST_RUNNER``::
    TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
    """
    def setup_test_environment(self, **kwargs):
        _set_eager()
        super(CeleryTestSuiteRunner, self).setup_test_environment(**kwargs)

