"""
CoinmarketCap api classes
"""
import requests


class CoinmarketCapApi:
    identifier = 'coinmarketcap'
    base = 'https://api.coinmarketcap.com/v1'
    requests_per_minute = 10

    def __init__(self, redis):
        self.redis = redis

    def get(self, resource):
        
        return requests.get('{}/{}'.format(base, resource))