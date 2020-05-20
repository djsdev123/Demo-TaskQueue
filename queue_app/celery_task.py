from celery import Celery
import time

app = Celery('taskq', broker='amqp://rabbit_queue', backend='redis://redis_queue')

@app.task(bind=True)
def reverse(self, string):
    self.update_state(state='PROGRESS')
    time.sleep(20)
    return string[::-1]

