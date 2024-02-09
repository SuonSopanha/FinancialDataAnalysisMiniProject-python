# STEP 3

# Import necessary libraries and local module
import matplotlib.pyplot as plt
from plot import covid 

# Extract relevant columns for plotting from the 'covid' DataFrame
x = covid.index
s_y = covid[['SPY']]
i_y = covid[['IAU']]
d_y = covid[['DBA']]
t_y = covid[['TLT']]

# Create subplots with 1 row and 3 columns
fig, axes = plt.subplots(1, 3, figsize=(10, 5))

# Plotting the data for each ticker on separate subplots
axes[0].plot(x, s_y, label='SPY')
axes[0].set_title('SPY')

axes[1].plot(x, i_y, label='IAU')
axes[1].set_title('IAU')

axes[2].plot(x, d_y, label='DBA')
axes[2].set_title('DBA')

# Adding a title to the entire figure
fig.suptitle('Covid 19')


plt.show()
