import yfinance as yf
aapl = yf.Ticker('AAPL')
aapl_info = aapl.info

print('AAPL sector: ', aapl_info['sector'])
print('AAPL EBITA Margins: ', aapl_info['ebitdaMargins'])
print('AAPL Profit Margins: ', aapl_info['profitMargins'])
print('AAPL Gross Margins: ', aapl_info['grossMargins'])
print('AAPL Day High: ', aapl_info['dayHigh'])

#aapl_history_max = aapl.history(period='max')
#aapl_history_max.head()

aapl_history_1m = aapl.history(start="2024-10-01", end="2024-10-15", interval="2m")
aapl_history_1m.head()