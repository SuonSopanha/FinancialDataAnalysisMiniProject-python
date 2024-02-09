# STEP 7

# Import the 'stock' DataFrame from 'tickerName'
from tickerName import stock
import matplotlib.pyplot as plt

# Calculate the daily percentage change in closing prices for all stocks in 'stock'
stock_daily_pc = (stock - stock.shift(1)) / stock.shift(1) * 100
print(stock_daily_pc.head())

# Calculate the cumulative sum of daily percentage changes for all stocks
stock_daily_cr = stock_daily_pc.cumsum()
print(stock_daily_cr)

# Plot the cumulative sum of daily percentage changes for all stocks
stock_daily_cr.plot(figsize=(20, 10))
plt.show()
