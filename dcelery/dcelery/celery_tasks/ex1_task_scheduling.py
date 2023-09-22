from datetime import timedelta
from dcelery.celery_config import app
from celery.schedules import crontab


app.conf.beat_schedule = {
    'task1': {
        'task': 'dcelery.celery_tasks.ex1_task_scheduling.task1',
        'schedule': crontab(minute=34, hour=19, day_of_week='mon-fri'),
    },
    'task2': {
        'task': 'dcelery.celery_tasks.ex1_task_scheduling.task2',
        'schedule': timedelta(seconds=8),
    }
}


@app.task(queue='tasks')
def task1():
    print('CRODGHFJKJBJDH,FVXGDGKHFJ')


@app.task(queue='tasks')
def task2():
    print('doing task 2')
