import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

# app.conf.task_routes = {
#     'api.tasks.*': {'queue': 'file_processing'},
# }

app.autodiscover_tasks()
