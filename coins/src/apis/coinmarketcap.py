"""
CoinmarketCap api classes
"""
import json
from .api import ThrottledJsonApi, Producer


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


class CoinmarketcapProducer(Producer):
    """
    class responsible for the data production
    """

    def produce(self):
        """
        run the job
        """
        data = self.api.get('ticker')
        for coin in data:
            print(coin)
            self.kafka_producer.send(
                topic="coins",
                value=json.dumps(coin)
            )
        self.kafka_producer.flush()
