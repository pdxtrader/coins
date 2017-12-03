"""
Celery app
"""
from celery import Celery
from celery.schedules import crontab


APP = Celery(
    'celery',
    broker='amqp://admin:mypass@rabbit:5672',
    backend='rpc://',
    include=['src.scrapers.tasks']
)

APP.conf.beat_schedule = {
    'coindesk': {
        'task': 'src.scrapers.tasks.coindesk_scrape',
        'schedule': crontab(minute="*/10"),
    },
}
