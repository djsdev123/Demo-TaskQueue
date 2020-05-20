from celery import Celery


app = Celery(
    'taskq',
    broker='amqp://rabbit_queue',
    backend='redis://redis_queue',
    include=[
        'celery_worker.celery_task'
    ]
)