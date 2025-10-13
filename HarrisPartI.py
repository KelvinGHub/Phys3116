# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading in the data
data= pd.read_csv('HarrisPartI.csv')

print(f"Total Clusters: {len(data)}")

#Plot 1: Galactic Coordinates (L,B)
plt.scatter(data['L'], data['B'])
plt.xlabel('Galactic Longitude (L)')
plt.ylabel('Galactic Latitude (B)')
plt.title('Galactic Coordinates of Clusters')
plt.grid()

plt.show()

#Plot 2: Distance from Galactic Center
plt.hist(data['R_gc'], bins=20, color='orange', edgecolor='black')
plt.xlabel('Distance from Galactic Center (R_gc)')
plt.ylabel('Number of Clusters')
plt.title('Distribution of Clusters from Galactic Center')
plt.grid()

plt.show()

#Plot 3: Spatial Distribution (X vs Y)
plt.scatter(data['X'], data['Y'])
plt.xlabel('X Coordinate (kpc)')
plt.ylabel('Y Coordinate (kpc)')
plt.title('Spatial Distribution of Clusters (X vs Y)')
plt.grid()

plt.show()




