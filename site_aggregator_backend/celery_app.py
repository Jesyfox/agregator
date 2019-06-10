from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

import celery_config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_agregator.settings')

app = Celery('site_agregator')

app.config_from_object(celery_config)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#  celery -A site_parser worker --loglevel=info
