import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

prices = pd.read_csv('prices.csv', index_col='Date', 
                     parse_dates=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

returns = prices.pct_change().dropna()

volatility = returns.std()*252**0.5
avg_return = returns.mean()*252

summary = pd.DataFrame({'Annual Return': avg_return,
                     'Annual Volatility': volatility})
summary['Return/Risk']= summary['Annual Return']/summary['Annual Volatility']
print(summary)

corr = returns.corr()
print(corr)

cumulative = (1+returns).cumprod()

cumulative.plot(figsize=(10, 6), title="Growth of ₹1")
plt.savefig('cumulative_returns.png')
plt.show()

sns.heatmap(corr, annot=True, cmap='coolwarm', vmax=1, vmin=1)
plt.title('Correlation of Daily Returns')
plt.savefig('correlation_heatmap.png')
plt.show()

sns.histplot(returns['RELIANCE.NS'], bins=50)
plt.title('Reliance daily returns')
plt.savefig('reliance_hist.png')
plt.show()

portfolio = returns.drop(columns="^NSEI").mean(axis=1)
port_vol = portfolio.std() * 252 ** 0.5
port_ret = portfolio.mean() * 252
print(port_ret, port_vol)