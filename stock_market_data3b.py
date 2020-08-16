# NOTE
# Using the Public Yahoo API (without authentication), you are limited to 2,000 requests per hour,
# or up to a total of 48,000 requests per day (based on IP address).

import pandas as pd 
import pandas_datareader.data as data

# asx200 data from https://www.asx200list.com
# The fieldname we are interested in is "Code" 
asx200 = pd.read_csv('asx200.csv')

# print header
print('Ticker\tP/E\t\tP/B\t\tDivY')

# retrieve the data for each ticker symbol and analyse the result
for code in asx200['Code'].values:
	# add '.AX' as suffix to ASX200 symbol codes for YahooFinance compatibility
	ticker_stats = data.YahooQuotesReader(code + '.AX').read()
	
	try:
		pe = ticker_stats['trailingPE'].values[0]
		pb = ticker_stats['priceToBook'].values[0]
		dy = ticker_stats['trailingAnnualDividendYield'].values[0]

		# scan for P/E ratio < 10, P/B ratio < than 1, and DY > 5% 
		if pe < 10 and pb < 1 and dy > 0.05:
			print('{}\t\t{:.2f}\t{:.4f}\t{:.4f}'.format(code, pe, pb, dy))

	except KeyError:
		# ignore tickers that don't have all of the targeted ticker stats
		pass
		




