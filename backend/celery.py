from celery import Celery

app = Celery('backend',
             broker='amqp://',
             backend='amqp://',
             include=['backend.tasks'])

app.conf.update(
    result_expires=3600,
    task_serializer='pickle',
    accept_content='application/x-python-serialize'
)

if __name__ == '__main__':
    app.start()