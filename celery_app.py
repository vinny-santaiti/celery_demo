from celery import Celery

app = Celery('my_celery',
             broker='amqp://guest:guest@localhost/',
             backend='rpc://',
             include=['celery_demo.tasks'])