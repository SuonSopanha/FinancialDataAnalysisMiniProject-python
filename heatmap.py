# STEP 8

# Import the 'stock' DataFrame from 'tickerName'
from tickerName import stock
import matplotlib.pyplot as plt

# Calculate the daily percentage change in closing prices for all stocks in 'stock'
stock_daily_pc = (stock - stock.shift(1)) / stock.shift(1) * 100

# Calculate the correlation matrix for the daily percentage changes
df_corr = stock_daily_pc.corr()
print(df_corr)

# Plot the correlation matrix as a heatmap
plt.imshow(df_corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(df_corr)), df_corr.columns, rotation='vertical')
plt.yticks(range(len(df_corr)), df_corr.columns)

# Set the size of the plot
plt.gcf().set_size_inches(10, 10)
plt.show()

# Scatter plot between correlation of SPY and VT
plt.scatter(df_corr.SPY, df_corr.VT)
plt.show()
