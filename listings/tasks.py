# listings/tasks.py
from celery import shared_task

@shared_task
def dummy_task():
    return "task works"
