from alphavantageinput import alphavantage_data

class StockPriceTimeSeries:
    def __init__(self,stock):
        self.dataset = alphavantage_data(stock)
        self.startTime = self.dataset.iloc[-1]
        self.currentValues = self.dataset.iloc[0]