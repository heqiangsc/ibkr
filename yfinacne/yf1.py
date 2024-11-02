import yfinance as yf
from sqlalchemy import create_engine
import mysql.connector
import sys
import os
import json

import datetime
import time

# 此段代码为基础设置，需要的主类就需要引入此段代码 -- begin --

num = len(sys.argv) - 1  # 参数个数
if num < 1:
    exit("参数错误,必须传环境变量!比如: python3 xx.py dev|pro|test")

print(sys.argv[1])
params = json.loads(sys.argv[1])


begin_date = params['begin'] if "begin" in params else None  # 开始时间
end_date = params['end'] if "end" in params else None  # 结束时间
file_name = params['file_name'] if 'file_name' in params else None
contractSymbol = params['cs'] if 'cs' in params else None
interval = params['interval'] if 'interval' in params else None




engine = create_engine("mysql+mysqlconnector://root:R3OzbedF!wi!@47.254.66.136:31321/yfinance?charset=utf8")
aapl = yf.Ticker(contractSymbol)
#获取股票的history数据
aapl_history_2m = aapl.history(start=begin_date, end=end_date, interval=interval)
aapl_history_2m.rename(columns={'Datetime': 'date', 'Open': 'open',
                                'Close': 'close', 'High': 'high',
                                'Low': 'low',
                                'Volume': 'volume', 'Dividends': 'dividends',
                                'Stock Splits': 'stock_splits'}, inplace=True)
aapl_history_2m['ticker'] = contractSymbol;
aapl_history_2m['interval'] = interval;


aapl_history_2m.to_sql('tticker', engine, if_exists="append")
print(aapl_history_2m.head())
