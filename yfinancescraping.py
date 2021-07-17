import yfinance as yf
import pandas as pd

from yahoo_fin.stock_info import get_data

bvsp = yf.Ticker("^BVSP")
hist = bvsp.history(period="5y")

hist.to_excel("output.xlsx")

dfs = pd.read_excel("output.xlsx", sheet_name=None)


bvsp2 = get_data('^BVSP', start_date = '16/07/2016', end_date = '16/07/2021', index_as_date = False, interval = "1d")



#f = open("histBVSP.txt", "w")
#f.write(hist)
#f.close()