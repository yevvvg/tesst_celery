from celery import shared_task

@shared_task
def task2():
    return