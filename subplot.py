# STEP 5

# Import necessary libraries and functions
from main import get_data
import matplotlib.pyplot as plt
import datetime
from datetime import date, datetime, time, timezone

# Retrieve historical stock data for ticker 'PDBC' from January 1, 2020, to the current date
data = get_data('PDBC', datetime(2020, 1, 1), datetime.today())

# Create a figure with two subplots for closing prices and volume
fig = plt.figure(figsize=(12, 8))

# Define top grid for closing prices and bottom grid for volume
top_grid = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
bottom_grid = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)

# Plot closing prices on the top grid
top_grid.plot(data.index, data['Close'], label='Close')

# Plot volume on the bottom grid
bottom_grid.plot(data.index, data['Volume'], label='Volume')


plt.tight_layout()

plt.legend()

plt.show()
