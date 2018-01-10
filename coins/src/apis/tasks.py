"""
Api parsing tasks
"""
from ..tools import get_kafka_producer, get_redis_connection
from ..celery.celery import APP
from .coinmarketcap import CoinmarketcapApi, CoinmarketcapProducer

@APP.task
def scrape(producer):
    """
    run a scraper
    """
    return producer.produce()

@APP.task
def coinmarketcap_scrape():
    """
    Coinmarketcap scraping
    """
    return scrape(
        CoinmarketcapProducer(get_kafka_producer(), CoinmarketcapApi(get_redis_connection()))
    )
