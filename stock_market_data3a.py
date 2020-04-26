import pandas as pd 
import pandas_datareader.data as data

# get the per share stats for the ticker
symbol = 'COL.AX'
ticker_stats = data.YahooQuotesReader(symbol).read()


# list some example per share stats for the ticker
pe = ticker_stats['trailingPE'].values[0]
pb = ticker_stats['priceToBook'].values[0]
dy = ticker_stats['trailingAnnualDividendYield'].values[0]

print('Ticker\t\tP/E\t\tP/B\t\tDivY')
print('{}\t\t{:.2f}\t{:.4f}\t{:.4f}').format(symbol, pe, pb, dy)

# to see a list of all the column names, issue the command:
# print ticker_stats.columns


