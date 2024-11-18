import requests
import pandas as pd
from io import StringIO
import backtrader as bt
import yfinance as yf
import json

args = { "tickers":"AAPL",  "start":"2024-10-01",  "end":"2024-10-20" }
url = 'https://sh.hesc.shop:453/yfd?test=false'
response = requests.post(url, json=args)
data = response.json()
df = pd.read_json(StringIO(data),encoding="utf-8", orient='records')
df['Price Date']=df['date']
df.set_index("Price Date",inplace=True)
df.drop(columns='date',inplace=True)
print(df.head())


