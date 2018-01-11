"""
Util functions
"""
from ..proto.candlestick_pb2 import _CANDLESTICK_COIN, _CANDLESTICK_EXCHANGE


def get_all_exchange_names() -> list:
    """
    get all exchange names in
    """
    return [name for name in _CANDLESTICK_EXCHANGE.values_by_name]

def get_all_coin_names() -> list:
    """
    get all coins defined in our protobuf schema
    """
    return [name for name in _CANDLESTICK_COIN.values_by_name]