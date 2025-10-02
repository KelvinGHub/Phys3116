import numpy as np
stellar_data = np.loadtxt('/Users/kelvinchen/Downloads/HarrisPartI.csv', delimiter=',', skiprows=1, dtype=object)
print(stellar_data)
ID = stellar_data[:,0]
Name=stellar_data[:,1]
RA=stellar_data[:,2]
Dec=stellar_data[:,3]
L=stellar_data[:,4]
B=stellar_data[:,5]
R_Sun=stellar_data[:,6]
R_gc=stellar_data[:,7]
X=stellar_data[:,8]
Y=stellar_data[:,9]
Z=stellar_data[:,10]
print(X)



