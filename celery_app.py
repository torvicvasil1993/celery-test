""" from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    result = add.delay(4, 4)
    print(f'Result: {result.get()}') """
