"""
Parsing tasks
"""
import os
import time
from redis import Redis
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from ..celery.celery import APP
from .scraper import Scraper
from .websites.coindesk import CoinDeskMainPage


@APP.task
def scrape(mainpage):
    """
    run a scraper
    """
    redis = Redis(os.environ.get('REDIS_HOST', 'localhost'), db=0)
    attempts = 0
    while True and attempts < 5:
        try:
            producer = KafkaProducer(
                bootstrap_servers=os.environ.get('KAFKA_HOST', '0.0.0.0') + ':9092',
                value_serializer=lambda v: v.encode('utf-8')
            )
            break
        except NoBrokersAvailable:
            print("Could not connect to kafka trying again in 5sec")
            attempts += 1
            time.sleep(5)
            if attempts >= 5:
                print("Could not connect to kafka, are you sure you set up KAFKA_HOST correctly?")
                raise
    scraper = Scraper(mainpage, redis=redis, kafka_producer=producer)
    return scraper.run()

@APP.task
def coindesk_scrape():
    """
    Coindesk scraping
    """
    return scrape(CoinDeskMainPage())
