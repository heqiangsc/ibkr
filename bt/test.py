import datetime as dt
fromdate = '2024-10-10'
dd = dt.datetime.strptime(fromdate, '%Y-%m-%d')
print(dd)
print(type(dd))
dd = dt.datetime.strftime(dd, '%Y-%m-%d')
print(dd)
print(type(dd))
