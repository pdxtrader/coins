"""
Base trader
"""
from .exchange import Order, Exchange


class Trader:
    """
    Generic trader function
    """
    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    def trade(self, order: Order) -> bool:
        """
        Trade on an order
        """
        pass
