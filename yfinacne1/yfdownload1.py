import yfinance as yf
import json
import argparse

args = '{ "tickers":"MSFT",  "start":"2024-06-01",  "end":"2024-10-20" }'
#获取股票的history数据
#aapl_history_1m = yf.download(args)
#print(aapl_history_1m.head())




def get_args_from_json(json_str):
    import json
    summary_dict = json.loads(json_str)
    arg = ''
    for key in summary_dict.keys():
        #args_dict[key] = summary_dict[key]
        arg += '{0}="{1}",'.format(key,summary_dict[key])
    return arg[:-1]


parser = argparse.ArgumentParser(description='Hello world')
args_dict = vars(parser.parse_args())
args1 = get_args_from_json(args)
print(  'yf.download({})'.format(args1)   )

#获取股票的history数据
aapl_history_1m = exec('yf.download({})'.format(args1))
print(aapl_history_1m.head())