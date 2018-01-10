"""
Shared functions
"""
import time
import os
from redis import Redis
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


def get_kafka_producer(
        kafka_host=os.environ.get('KAFKA_HOST', 'kafka'), port=9092,
        max_attempts=5, delay=5):
    """
    get kafka producer, with max_attempts retries
    """
    attempts = 0
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers="{}:{}".format(kafka_host, port),
                value_serializer=lambda v: v.encode('utf-8')
            )
            break
        except NoBrokersAvailable:
            print("Could not connect to kafka ({}) trying again in {}sec".format(kafka_host, delay))
            attempts += 1
            time.sleep(delay)
            if attempts >= max_attempts:
                print("KAFKA_HOST= {} :Could not connect to kafka".format(kafka_host))
                raise
    return producer


def get_redis_connection(redis_host=os.environ.get('REDIS_HOST', 'localhost'), port=6378):
    """
    get redis connection
    """
    return Redis(redis_host, port=port)
