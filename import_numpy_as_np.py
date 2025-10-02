import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import cmasher as cm
stellar_data = np.loadtxt('Krause21.csv', delimiter=',', skiprows=1, dtype=object)
Age = stellar_data[:,6]
FeH = stellar_data[:,7]
cmap = colours.ListedColormap(['blue', 'green', 'red'])
cmap_2 = cm.tropical
plt.scatter(Age.astype(float), FeH.astype(float))
plt.xlabel('Age')
plt.ylabel('FeH')
plt.title('Age vs FeH')
plt.show()

