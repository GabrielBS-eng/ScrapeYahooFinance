import yfinance as yf
import pandas as pd

from yahoo_fin.stock_info import get_data

bvsp = yf.Ticker("^BVSP")
hist = bvsp.history(period="5y")

hist.to_excel("output.xlsx")

dfs = pd.read_excel("output.xlsx", sheet_name=None)


bvsp2 = get_data('^BVSP', start_date = '16/07/2016', end_date = '16/07/2021', index_as_date = False, interval = "1d")
bvsp2['month']=pd.DatetimeIndex(bvsp2.date).month
bvsp2['year']=pd.DatetimeIndex(bvsp2.date).year

mLog = pd.DataFrame(columns=['Date', 'logRet', 'volume'])
log = 0
value = 0

for i in bvsp2.index:
    if bvsp2.index[0]==0:
        month=bvsp2["month"][0]
        year=bvsp2["year"][0]

#        mLog.append(pd.DataFrame([pd.to_datetime(pd.DataFrame({'year': [year], 'month': [month], 'day': [1]})), log, value], columns=['Date', 'logRet', 'volume']))

    if month==bvsp2["month"][i] and year==bvsp2["year"][i]:
        print('hi')


#f = open("histBVSP.txt", "w")
#f.write(hist)
#f.close()