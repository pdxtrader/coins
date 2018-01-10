"""
Binance Client
"""
from binance.client import Client
from .exchange import Exchange
from ..proto.candlestick_pb2 import Candlestick

SYMBOLS = set(['ETH', 'LTC', 'DASH', 'XMR','ADA'])

API_KEY = 'uyMFg2uqzPcYCelTWYXVkzUOFFTx82p3O0qj5loEKJdLB6fJHquB82evKjHnB0No'
API_SECRET = '6dxBxjG4MG8op3lucssgE4kuVjmpq0K8ZpExhwx1ES5rIsMsxmnM8ci0CUdlKZFl'

def coins_to_symbol(source: str, target: str):
    return "{}{}".format(source, target)

class Binance(Exchange):
    """
    Binance Client
    """
    def __init__(self, client: Client, socket_manager=None):
        self.client = client
        self.socket_manager = socket_manager

    def start_collecting(self) -> bool:
        """
        start collecting data about trades
        """

        pass

    def publish(self, candlestic: Candlestick) -> bool:
        """
        publish trade to kafka
        """
        self.kafka_producer.send(
            topic="candlesticks",
            value=candlestic.SerializeToString()
        )