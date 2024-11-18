import backtrader as bt
import yfinance as yf
from yfinacne1.myyf import request_yf
import json


# Create a subclass of bt.Strategy


# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
#cerebro.addstrategy(TestStrategy)

# Create a Data Feed


#data = bt.feeds.PandasData(dataname=yf.download("MSFT",
#                                                start="2024-06-01",
#                                                end="2024-10-20"))

# data_df = yf.download(tickers="MSFT",  start="2024-06-01", end="2024-10-20")
# print(data_df)
# data_df.columns = data_df.columns.droplevel(1)

args = { "tickers":"MSFT",  "start":"2024-10-01",  "end":"2024-10-20" }
df = request_yf(args)
data = bt.feeds.PandasData(dataname=df)
print(data)
# Add the Data Feed to Cerebro
cerebro.adddata(data)
# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

# Set the commission
cerebro.broker.setcommission(commission=0.001)

# Run over everything
cerebro.run()

# Plot the result
cerebro.plot()
