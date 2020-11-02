from stockprices import StockPriceTimeSeries
from active_stocks import Listings

class Exchange:
    def __init__(self):
        self.name = "KOBEX"
        print("Welcome at %s" %self.name)

    def available_stocks(self):
        listings = Listings()
        symbol = listings.get_symbol()
        return symbol

    def stock_price(self,stock):
        data = StockPriceTimeSeries(stock)
        return data.currentValues


