import yfinance as yf

bvsp = yf.Ticker("^BVSP")
hist = bvsp.history(period="5y")