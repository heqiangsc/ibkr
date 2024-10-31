import yfinance as yf
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:R3OzbedF!wi!@47.254.66.136:3306/yfinance?charset=utf8mb4")
aapl = yf.Ticker('AAPL')
#获取股票的history数据
aapl_history_2m = aapl.history(start="2024-10-01", end="2024-10-15", interval="2m")
aapl_history_2m.to_sql("aapl_history_2m", engine, index=False)
print(aapl_history_2m.head())
