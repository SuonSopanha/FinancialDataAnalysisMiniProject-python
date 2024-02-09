# STEP 4

# Import necessary libraries and functions
from main import get_data
import matplotlib.pyplot as plt
import datetime
from datetime import date, datetime, time, timezone

# Retrieve historical stock data for ticker 'PDBC' from January 1, 2020, to the current date
data = get_data('PDBC', datetime(2020, 1, 1), datetime.today())

# Drop unnecessary columns from the DataFrame for volume analysis
data.drop(['Ticker', 'High', 'Low', 'Open', 'Close', 'Adj Close'], axis=1, inplace=True)

# Extract date index and volume data for plotting
x = data.index
y = data['Volume']

# Create a bar plot to visualize the volume trend over time
plt.figure(figsize=(15, 3))
plt.bar(x, y)

plt.show()


