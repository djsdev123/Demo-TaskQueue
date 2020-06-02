from celery import Celery


app = Celery(
    'taskq',
    broker='amqp://rabbit_queue',
    backend='redis://redis_queue',
    include=[
        'celery_worker.celery_task'
    ]
)

# app = Celery(
#     'taskq',
#     broker='amqp://localhost',
#     backend='redis://localhost',
#     include=[
#     	'celery_worker.celery_task'
#     ]
# )