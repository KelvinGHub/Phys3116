
#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import cmasher as cm

stellar_data = np.loadtxt('Krause21.csv', delimiter=',', skiprows=1, dtype=object)

star_T = stellar_data[:,0].astype(float) # teperature in Kelvin
star_L = stellar_data[:,1].astype(float) # luminosity in solar luminosity
star_R = stellar_data[:,2].astype(float) # radius in solar radii
star_Mv = stellar_data[:,3].astype(float) # magnitude of star
star_type = stellar_data[:,4] # star type
star_colour = stellar_data[:,5] # colour of star

Age = stellar_data[:,6]
FeH = stellar_data[:,7]

cmap = colours.ListedColormap(['blue', 'green', 'red'])
cmap_2 = cm.tropical
plt.scatter(Age.astype(float), FeH.astype(float))
plt.xlabel('Age')
plt.ylabel('FeH')
plt.title('Age vs FeH')
plt.show()

