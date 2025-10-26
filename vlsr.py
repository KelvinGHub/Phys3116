import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df_harris3 = pd.read_csv('HarrisPartIII.csv', usecols=['ID', 'v_LSR'])
df_harris3clean = df_harris3.dropna(subset=['v_LSR'])
df_accreted = df_harris3clean[(df_harris3clean['v_LSR'] > 100) | (df_harris3clean['v_LSR'] < -100)]
print("Potentially accreted clusters based on |v_LSR| > 100 km/s:")
print(df_accreted)
plt.figure(figsize=(8,5))
plt.hist(df_harris3clean['v_LSR'].dropna(), bins=100, color='skyblue', edgecolor='black')
plt.xlabel('v_LSR (km/s)')
plt.ylabel('Number of Clusters')
plt.title('Histogram of Galactic Velocity of Globular Clusters')
plt.show()