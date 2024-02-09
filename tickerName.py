# STEP 2

# Import necessary libraries
import pandas as pd

# Import the get_data function, start, and end variables from the main module
from main import get_data, start, end

# Use the get_data function to fetch historical stock data for different tickers
SPY = get_data('SPY', start, end)
ITW = get_data('ITW', start, end)
VT = get_data('VT', start, end)
DBA = get_data('DBA', start, end)
TLT = get_data('TLT', start, end)
PDBC = get_data('PDBC', start, end)
IAU = get_data('IAU', start, end)

# Pivot the DataFrames to have 'Close' prices for each ticker as columns
SPY = SPY.pivot(columns="Ticker", values="Close")
ITW = ITW.pivot(columns="Ticker", values="Close")
VT = VT.pivot(columns="Ticker", values="Close")
DBA = DBA.pivot(columns="Ticker", values="Close")
TLT = TLT.pivot(columns="Ticker", values="Close")
PDBC = PDBC.pivot(columns="Ticker", values="Close")
IAU = IAU.pivot(columns="Ticker", values="Close")

# Concatenate the individual DataFrames into a single DataFrame 'stock'
stock = pd.concat([SPY, ITW, VT, DBA, TLT, PDBC, IAU], axis=1, join='outer')

# The 'stock' DataFrame now contains 'Close' prices for different tickers in a single DataFrame
# You can use this DataFrame for further analysis or visualization
