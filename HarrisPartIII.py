# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading in the data
data = pd.read_csv('HarrisPartIII.csv')
data=data[(data['v_r']>-999)&(data['v_LSR']>-999)&(data['sig_v']>0)] #remove bad data

#plotting the data
#v_LSR vs velocity dispersion
plt.subplot(1,2,1)
plt.scatter(data['v_LSR'], data['sig_v'], marker='.')

# Labeling the plot
plt.title(r'Velocity Dispersion vs LSR Velocity for Globular Clusters')
plt.xlabel(r'v$_{LSR}$ (km/s)')
plt.ylabel(r'Velocity Dispersion, $\sigma_v$ (km/s)')


#radial velocity vs rotation
plt.subplot(1,2,2)
plt.scatter(data['v_LSR'], data['v_r'], marker='.')
# Labeling the plot
plt.title(r'Ratation vs Radial Velocity for Globular Clusters')
plt.xlabel(r'v$_{LSR}$ (km/s)')
plt.ylabel(r'Radial Velocity, v$_r$ (km/s)')

plt.show()
