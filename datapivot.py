#STEP 1

from main import yahooData ,get_data

dataPivot = yahooData.pivot(columns='Ticker', values='Close')

print(dataPivot.head())