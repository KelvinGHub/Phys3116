import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import scipy.stats as stats
from scipy.stats import norm 

def starter():
    df = pd.read_csv('Krause21.csv')
    print("Data Loaded:", len(df), "clusters")
    return df

df = starter()
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['FeH'], color='grey', label='Globular Clusters')

plt.xlabel('Age (Gyr)')
plt.ylabel('[Fe/H]')
plt.title('Globular Clusters Age vs [Fe/H]')
plt.legend()
plt.tight_layout()
plt.gca()
plt.show()