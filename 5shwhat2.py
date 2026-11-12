import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

prices = pd.read_csv('prices.csv', index_col='Date', parse_dates=True)

prices=prices.dropna()

returns = prices.pct_change().dropna()
print(returns.head())
print(returns.describe())

print(returns['RELIANCE.NS'].idxmax())
print(returns['LT.NS'].idxmin())