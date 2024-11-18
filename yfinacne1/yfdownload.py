import yfinance as yf
aapl = yf.Ticker('AAPL')
aapl_info = aapl.info

print('AAPL sector: ', aapl_info['sector'])
print('AAPL EBITA Margins: ', aapl_info['ebitdaMargins'])
print('AAPL Profit Margins: ', aapl_info['profitMargins'])
print('AAPL Gross Margins: ', aapl_info['grossMargins'])
print('AAPL Day High: ', aapl_info['dayHigh'])

aapl_history_max = aapl.history(period='max')
print(aapl_history_max.head())

#获取股票的history数据
aapl_history_1m = aapl.history(start="2024-10-01", end="2024-10-15", interval="2m")
print(aapl_history_1m.head())

#获取股票的分红和扩股数据
aapl_actions = aapl.actions
print(aapl_actions.head())