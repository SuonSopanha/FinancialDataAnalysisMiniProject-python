# STEP 1

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf

import datetime

from datetime import date, datetime, time, timezone

# Define a function to fetch stock data using Yahoo Finance
def get_data(ticker, start_date, end_date):
    # Use yfinance to download historical stock data for the specified ticker and date range
    df = yf.download(ticker, start=start_date, end=end_date)
    
    # Insert a new column 'Ticker' at the beginning of the DataFrame with the specified ticker
    df.insert(0, 'Ticker', ticker)
    
    return df

# Specify the stock ticker, start date, and end date for fetching the data
ticker = 'DIS'
start = datetime(2020, 1, 1)
end = datetime.today()

# Call the get_data function to fetch stock data for Disney (DIS) from Yahoo Finance
yahooData = get_data(ticker, start, end)


