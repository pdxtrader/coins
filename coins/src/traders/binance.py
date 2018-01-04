"""
Binance Client
"""
from binance.client import Client as BinanceApiClient
from .base import Client

SYMBOLS = set(['YOYO', 'BCPT','BCD','CTR','QTUM','TRX','BCC','LEND','FUN','ENJ','HSR','KNC','MDA','VIB','XMR','QSP','BTC','SUB','MOD','WABI','GXS',
'BQX','GVT','123','TRIG','DASH','MTL','ICN','XLM','SALT','ZRX','ARK','ETH','DGD','LINK','BNT','RCN','XZC','POE','XRP','SNM','OAX','MANA','CDT',
'EVX','POWR','ZEC','USDT','KMD','LRC','AMB','OMG','NEO','LUN','DNT','BNB','EDO','XVG','FUEL','ENG','NAV','GTO','IOTA','OST','AION','BRD','REQ',
'PPT','BTS','ARN','RDN','GAS','VEN','NEBL','LSK','ADX','AST','WTC','BTG','STORJ','TNT','MTH','SNT','STRAT','456','CND','ICX','NULS','MCO','SNGLS',
'ETC','LTC','WAVES','WINGS','DLT','ELF','BAT','CMT','TNB','EOS','ADA'])

class BinanceClient(Client, BinanceApiClient):
    """
    Binance Client
    """
    def prices(self) -> list:
        """
        all prices
        """
        tickers = self.get_all_tickers()

    def price_of(self, source: str, target: str) -> float:
        