#!/usr/bin/env python

import time
import json
import os
from src.scraper import Scraper
from src.coindesk import CoinDeskMainPage
from redis import Redis
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


if __name__ == '__main__':
    redis = Redis(os.environ.get('REDIS_HOST', 'localhost'), db=0)
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=os.environ.get('KAFKA_HOST', '0.0.0.0') + ':9092',
                value_serializer=lambda v: v.encode('utf-8')
            )
            break
        except NoBrokersAvailable as e:
            print("Could not connect to kafka trying again in 5sec")
            time.sleep(5)

    scrapers = [
        Scraper(CoinDeskMainPage(), redis=redis, kafka_producer=producer)
    ]

    while True:
        for scraper in scrapers:
            scraper.run()
        time.sleep(10)
