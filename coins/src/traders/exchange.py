"""
Exchange classes
"""
from ..proto.candlestick_pb2 import Candlestick

class Trade:
    """
    Trade in an exchange
    """

    def __init__(self, source: str, target: str, price: float):
        self.source = source
        self.target = target
        self.price = price

    def to_dict(self):
        """
        get dict representation of trade
        """
        return {
            "source": self.source,
            "target": self.target,
            "price": self.price
        }


class Order:
    """
    Order in an exchange
    """

    def __init__(self, source: str, target: str, price: float, is_sell: bool):
        self.source = source
        self.target = target
        self.price = price
        self.is_sell = is_sell


class Exchange:
    """
    Exchange class
    """

    def __init__(self, exchange_id: str, kafka_producer):
        self.kafka_producer = kafka_producer
        self.exchange_id = exchange_id

    def place_order(self, order: Order) -> bool:
        """
        trade a specific order
        """
        pass

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
