from celery import Celery
from celery.schedules import crontab
import datetime

app = Celery('myapp',
             broker='amqp://guest:guest@rabbitmq:5672//',
             backend='rpc://')

app.conf.timezone = 'America/Sao_Paulo'

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.mytask',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'add-every-morning': {
        'task': 'app.mytask',
        'schedule': crontab(hour=7, minute=30),
        'args': (4, 4)
    },
}

@app.task
def mytask(x, y):
    now = datetime.datetime.now()
    print(f"The current time in Brazil/Sao_Paulo is {now}")
    return x + y
    
