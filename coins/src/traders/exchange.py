"""
Exchange classes
"""
import json


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

    def __init__(self, exchange_id: int, kafka_producer):
        self.kafka_producer = kafka_producer
        self.exchange_id = exchange_id

    def buy_orders(self, source: str, target: str) -> list:
        """
        all buy orders for specific combination
        """
        pass

    def sell_orders(self, source: str, target: str) -> list:
        """
        all sell orders for specific combination
        """
        pass

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

    def publish(self, trade: Trade) -> bool:
        """
        publish trade to kafka
        """
        self.kafka_producer.send(
            topic="trades",
            value=json.dumps({
                "exchange_id": self.exchange_id,
                **trade.serialize()
            })
        )
