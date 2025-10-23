#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

#reading in the data
data = pd.read_csv('vandenBerg_table2.csv')
data = data[(data['Age'] > 0) & (data['FeH'] > -99)]

#plotting the data
plt.scatter(np.log10(data['Age']), data['FeH'], marker='.')

# linear regression
x_log=np.log10(data['Age'])
slope, intercept, r_value, p_value, std_err = stats.linregress(x_log, data['FeH'])
print(f"Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}")

# Plotting the regression line
x_fit = np.linspace(min(x_log), max(x_log), 100)
y_fit = intercept + slope * x_fit
plt.plot(x_fit, y_fit, color='red', label='Linear Fit')


# Labeling the plot
plt.title(r'Metallicity vs Age for Globular Clusters')
plt.xlabel('Age ($Gyr$)')
plt.ylabel(r'Fe/H')

plt.show()