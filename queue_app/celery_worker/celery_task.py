from celery_worker import app
import time
from celery import Task


# @app.task(bind=True)
# def reverse(self, string):
#     self.update_state(state='PROGRESS')
#     time.sleep(20)
#     return string[::-1]

class Reverse(Task):

	def run(self, string):
		res = self.logic(string)
		return res

	def logic(self, string):
		self.update_state(state='PROGRESS')
		time.sleep(20)
		return string[::-1]

reverse = app.register_task(Reverse())
