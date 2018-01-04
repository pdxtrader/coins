"""
Base trader
"""


class Client:
    """
    Exchange Client
    """
    def prices(self) -> list:
        """
        all latest prices
        """
        pass

    def price_of(self, source: str, target: str) -> float:
        """
        price of specific combination
        """
        pass

    def price_of_with_depth(self, source: str, target: str, max_depth: float) -> list:
        """
        list of dicts with prices and depth
        [{price: float, depth: float}, ...]
        """
        pass

    
class Trader:
    """
    Generic trader function
    """
    def __init__(self, client: Client):
        self.client = client

    def make_order(self, source: str, target: str, price: float) -> bool:
        """
        Create an order
        """
        pass

    def total_balance(self, currency: str) -> float:
        """
        get current balance of trader if it would be changed to <currency>
        """
        pass

    def sub_balance(self, currency: str) -> float:
        """
        current balance of <currency>
        """
        pass
