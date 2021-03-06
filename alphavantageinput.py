import requests, pandas as pd, itertools

def alphavantage_data(stock):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stock.strip()+"&interval=5min&outputsize=full&apikey=JT6K3CZJG0VVJQTR"
    response = requests.get(url)
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
    return df
