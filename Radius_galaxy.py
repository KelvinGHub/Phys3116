import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import scipy.stats as stats
from scipy.stats import norm 
df_hp = pd.read_csv('HarrisPartI.csv', usecols=['ID', 'R_gc'])
df_vb = pd.read_csv('vandenBerg_table2.csv')
df_vb['ID'] = 'NGC ' + df_vb['NGC'].astype(str)
df_vb = df_vb[['ID', 'Name', 'R_G']].rename(columns={'R_G': 'R_gc'})
df_hp['Name'] = None
df_hp = df_hp[['ID', 'Name', 'R_gc']]
df_all = pd.concat([df_hp, df_vb], ignore_index=True)
df_all = df_all.sort_values(by='ID').reset_index(drop=True)
df_all = df_all.sort_values(by=['ID', 'R_gc', 'Name'], key=lambda col: col.isnull() if col.name == "Name" else col)
df_all = df_all.drop_duplicates(subset=['ID', 'R_gc'], keep='first').reset_index(drop=True)
print("Total number of clusters with known R_gc:")
print(len(df_all))
df_15kpc = df_all[df_all['R_gc'] >= 15].sort_values(by='R_gc', ascending=False).reset_index(drop=True)
print(df_15kpc)
plt.figure(figsize=(8,5))
plt.hist(df_all['R_gc'].dropna(), bins=100, color='skyblue', edgecolor='black')
plt.xlabel('Radius (kpc)')
plt.ylabel('Number of Clusters')
plt.title('Histogram of Galactocentric Radii of Globular Clusters')
plt.show()
