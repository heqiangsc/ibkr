import backtrader as bt
from yfinacne1.myyf import request_yf



class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s,%s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        # 跟踪挂单
        self.order = None

    def notify_order(self, order):
        print('order:%s' % order.Margin)

        if order.status in [order.Submitted, order.Accepted]:
            # broker 提交/接受了，买/卖订单则什么都不做
            return
        # 检查一个订单是否完成
        # 注意: 当资金不足时，broker会拒绝订单
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('已买入, %.2f' % order.executed.price)
            elif order.issell():
                self.log('已卖出, %.2f' % order.executed.price)

                # 记录当前交易数量
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('订单取消/保证金不足/拒绝')

            # 其他状态记录为：无挂起订单
        self.order = None

    def next(self):
        # 记录收盘价
        self.log('Close, %.2f' % self.dataclose[0])

        # 如果有订单正在挂起，不操作
        if self.order:
            return

            # 如果没有持仓则买入
        if not self.position:
            # 今天的收盘价 < 昨天收盘价
            if self.dataclose[0] < self.dataclose[-1]:
                # 昨天收盘价 < 前天的收盘价
                if self.dataclose[-1] < self.dataclose[-2]:
                    # 买入
                    self.log('买入, %.2f' % self.dataclose[0])
                    # 跟踪订单避免重复
                    self.order = self.buy()
        else:
            # 如果已经持仓，且当前交易数据量在买入后5个单位后
            if len(self) >= (self.bar_executed + 5):
                # 全部卖出
                self.log('卖出, %.2f' % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.sell()
cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)
args = { "tickers":"AAPL",  "start":"2024-10-01",  "end":"2024-10-20" }
df = request_yf(args)
#data_yf = yf.download('MSFT', start='2024-10-01', end='2024-11-07')

# print(data_yf.head())
#data_yf.columns = data_yf.columns.droplevel(1)
# print(data_yf.head())
cerebro.adddata(bt.feeds.PandasData(dataname=df))

cerebro.broker.setcash(100000.0)
print('组合期初资金:%.2f' % cerebro.broker.getvalue())
cerebro.run()
print('组合期末资金:%.2f' % cerebro.broker.getvalue())