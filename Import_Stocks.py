#!/usr/bin/env python

from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
from datetime import datetime

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=['DJIA']
today = date.today()
start_date= time.strptime("2017/01/01", '%y/%m/%d')
#end_date=datetime.strftime('2019–11–30', '%y/%m/%d')
print(start_date)

# files=[]
# def getData(ticker_list):
#     print(ticker_list)
# data = pdr.get_data_yahoo(ticker_list, start=start_date, end=today)
# dataname= ticker+'_'+str(today)
# files.append(dataname)
# SaveData(data, dataname)
# # Create a data folder in your current dir.
# def SaveData(df, filename):
#     f.to_csv('./data/'+filename+'.csv')
# #This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
# for tik in ticker_list:
#     getData(tik)
# for i in range(0,11):
#     df1= pd.read_csv('./data/'+ str(files[i])+'.csv')
#     print (df1.head())