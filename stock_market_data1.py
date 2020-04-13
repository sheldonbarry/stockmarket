# extract basic stock data from yahoo

import datetime as dt
import pandas as pd
import pandas_datareader as pdr

# target stock details
stock_pick = '^AORD'
start_date = dt.datetime(2019,1,1)
end_date = dt.date.today()

# get stock data
df = pdr.DataReader(stock_pick, 'yahoo', start_date, end_date)

# print stock data 
print(df.tail())