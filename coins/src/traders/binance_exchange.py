"""
Binance Client
"""
from binance.client import Client
from .exchange import Exchange
from ..proto.candlestick_pb2 import Candlestick

API_KEY = 'uyMFg2uqzPcYCelTWYXVkzUOFFTx82p3O0qj5loEKJdLB6fJHquB82evKjHnB0No'
API_SECRET = '6dxBxjG4MG8op3lucssgE4kuVjmpq0K8ZpExhwx1ES5rIsMsxmnM8ci0CUdlKZFl'



class Binance(Exchange):
    """
    Binance Client
    """
    def __init__(self, client: Client, socket_manager=None, *args, **kwargs):
        self.client = client
        self.socket_manager = socket_manager
        super().__init__(*args, **kwargs)

    @classmethod
    def _get_all_websocket_names(cls) -> list:
        

    @classmethod
    def coins_to_symbol(cls, source: str, target: str) -> str:
        """
        binance accepts symbols as an input
        returns the symbol from source, target coins
        """
        return "{}{}".format(source, target)

    def start_collecting(self) -> bool:
        """
        start collecting data about trades
        """
        socket_manager.
        pass

    def publish(self, candlestic: Candlestick) -> bool:
        """
        publish trade to kafka
        """
        self.kafka_producer.send(
            topic="candlesticks",
            value=candlestic.SerializeToString()
        )