from celery_worker import app
import time


@app.task(bind=True)
def reverse(self, string):
    self.update_state(state='PROGRESS')
    time.sleep(20)
    return string[::-1]