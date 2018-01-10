"""
Parsing tasks
"""
import os
from redis import Redis
from ..tools import get_kafka_producer, get_redis_connection
from ..celery.celery import APP
from .scraper import Scraper
from .websites.coindesk import CoinDeskMainPage


@APP.task
def scrape(mainpage):
    """
    run a scraper
    """
    redis = get_redis_connection()
    scraper = Scraper(mainpage, redis=redis, kafka_producer=get_kafka_producer())
    return scraper.run()

@APP.task
def coindesk_scrape():
    """
    Coindesk scraping
    """
    return scrape(CoinDeskMainPage())
