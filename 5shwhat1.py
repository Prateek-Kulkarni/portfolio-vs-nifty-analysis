import pandas as pd
import yfinance as yf

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'TATASTEEL.NS', 'LT.NS', '^NSEI']

raw = yf.download(tickers, period='3y')
print(raw.shape)
print(raw.columns)

prices = raw['Close']

print(prices.head())
print(prices.tail())
print(prices.isna().sum())

prices.to_csv('prices.csv')
print(prices[prices["^NSEI"].isna()])