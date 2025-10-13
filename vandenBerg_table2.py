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
plt.scatter(data['Age'], data['FeH'], marker='.')
cbar = plt.colorbar()

# Labeling the plot
plt.title(r'Metallicity vs Age for Globular Clusters')
plt.xlabel('Age ($Gyr$)')
plt.ylabel(r'Fe/H')

plt.show()