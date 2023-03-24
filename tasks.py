from celery import Celery


#app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')


@app.task
def hello_world():
    return "Hello World"
