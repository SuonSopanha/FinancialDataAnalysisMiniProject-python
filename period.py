# STEP 9

# Import the 'stock' DataFrame from 'tickerName'
from tickerName import stock
import matplotlib.pyplot as plt

# Calculate the daily percentage change in closing prices for all stocks in 'stock'
stock_daily_pc = (stock - stock.shift(1)) / stock.shift(1) * 100

# Define the number of periods for rolling standard deviation
periods = 75

# Calculate the rolling standard deviation (volatility) for each stock
volatility = stock_daily_pc.rolling(periods).std()

# Print the calculated volatility
print(volatility)

# Plot the volatility for specific stocks (SPY, TLT, DBA)
volatility['SPY'].plot(label='SPY')
volatility['TLT'].plot(label='TLT')
volatility['DBA'].plot(label='DBA')

# Show the plot
plt.legend()
plt.show()
