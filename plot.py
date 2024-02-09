#STEP 3

import matplotlib.pyplot as plt
from tickerName import stock

#use matplolib to plot
plt.style.use('ggplot')
stock.plot(figsize=(10, 5))

#plt.show()


#get the data from 2020-02-01 to 2020-07-31
covid = stock['2020-02-01':'2020-07-31']
covid.plot(figsize=(10, 5))

#plt.show()

