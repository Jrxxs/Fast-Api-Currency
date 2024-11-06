import os
from celery import Celery


CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379")

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND, include="app.tasks")

celery_app.conf.beat_schedule = {
    'fetch-price-every-minute': {
        'task': 'app.tasks.currencies_api_request_task',
        'schedule': 60
    }
}
celery_app.conf.timezone = 'UTC'
