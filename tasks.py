from .celery_app import app
import time


@app.task()
def add(x, y):
    print('task begins')
    time.sleep(3)
    print('task finished')
    return x + y