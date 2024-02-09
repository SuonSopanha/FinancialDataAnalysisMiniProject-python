# STEP 6

# Import the 'stock' DataFrame from 'tickerName'
from tickerName import stock
import matplotlib.pyplot as plt

print(stock.head)
print(stock['SPY'])
print(stock['SPY'].shift(1))

# Calculate the daily percentage change in closing prices for 'SPY'
spy_daily_pc = (stock['SPY'] / stock['SPY'].shift(1) - 1) * 100
print(spy_daily_pc)

# Plot the histogram of daily percentage changes in closing prices for 'SPY'
plt.hist(spy_daily_pc, bins=50)
plt.show()
