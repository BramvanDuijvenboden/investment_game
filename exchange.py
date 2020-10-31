import requests, pandas as pd, itertools

class Exchange:
    def __init__(self):
        self.name = "KOBEX"
        print("Welcome at %s" %self.name)

    def available_stocks(self):
        stocks = {'Microsoft Corp' : 'MSFT'}

        print(stocks.keys())
        return 'MSFT' #temporary hard coded to prevent having to give input
        # choice = input("Choose a company:")
        # try:
        #     choice in stocks.keys()
        #     return stocks[choice]
        # except:
        #     print("Stock not available")



    def stock_price(self,stock):
        response = requests.get(
            "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stock+"&interval=5min&outputsize=full&apikey=demo")
        if response.status_code != 200:
            raise ValueError("Could not retrieve data, code:", response.status_code)
        raw_data = response.json()
        raw_data.keys()
        list(itertools.islice(raw_data['Time Series (5min)'].items(), 0, 5))

        colname = list(raw_data.keys())[-1]  # Let's be smart and retrieve the name of the column with our actual data
        data = raw_data[colname]  # We want to extract the corresponding column only
        df = pd.DataFrame(data).T.apply(pd.to_numeric)

        df.index = pd.DatetimeIndex(df.index)  # Next we parse the index to create a datetimeindex
        df.rename(columns=lambda s: s[3:], inplace=True)  # Let's fix the column names

        df['previous close'] = df['close'].shift(-1)
        df['return'] = ((df['close'] - df['previous close']) / df['previous close']) / 100
        print(df.iloc[0])
        return df.iloc[0]
