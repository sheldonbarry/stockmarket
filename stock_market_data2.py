# extract basic stock data from yahoo and graph the result

import datetime as dt
import pandas as pd
import pandas_datareader as pdr
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# register converters (otherwise a FutureWarning is thrown)
pd.plotting.register_matplotlib_converters()

# target stock details
stock_pick = '^AORD'
start_date = dt.datetime(2019,1,1)
end_date = dt.date.today()

# get stock data
df = pdr.DataReader(stock_pick, 'yahoo', start_date, end_date)

# print stock data 
print(df.tail())

# create a moving average column in the data
df['m_avg'] = df['Adj Close'].rolling(window=50).mean()

#set up axes for different graphs
ax1 = plt.subplot2grid((10,1), (0,0), rowspan=8, colspan=1)
plt.title(stock_pick)
# scale both graphs to ax1
ax2 = plt.subplot2grid((10,1), (9,0), rowspan=1, colspan=1, sharex=ax1)	

# graph data using date(index) as x axis
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['m_avg'])
ax2.bar(df.index, df['Volume'])

# format axis tick labels
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
# scale date ticks dynamically
plt.gcf().autofmt_xdate() 	

# save the plot image (optional)
plt.savefig('./chart.png')

# display the chart
plt.show()

