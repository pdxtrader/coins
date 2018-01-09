"""
Binance Client
"""
from binance.client import Client
from .exchange import Exchange

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

    def buy_orders(self, source: str, target: str) -> list:
        """
        all prices
        """
        return client. = self.get_all_tickers()

    def price_of(self, source: str, target: str) -> float:
        