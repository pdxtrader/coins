"""
CoinmarketCap api classes
"""
import json
from .api import ThrottledJsonApi


class CoinmarketcapApi(ThrottledJsonApi):
    """
    Api handler for coinmarketCap
    """
    def __init__(self, redis):
        self.redis = redis
        super().__init__(
            redis=redis,
            requests_per_minute=10,
            identifier='coinmarketcap',
            base='https://api.coinmarketcap.com/v1',
            available_resources=['ticker']
        )


class CoinmarketcapProducer(CoinmarketcapApi):
    """
    class responsible for the data production
    """
    def __init__(self, redis, kafka_producer):
        self.kafka_producer = kafka_producer
        super().__init__(
            redis
        )

    def run(self):
        """
        run the job
        """
        data = self.get('ticker')
        for coin in data:
            self.kafka_producer.send(
                topic="coins",
                value=json.dumps(coin)
            )
