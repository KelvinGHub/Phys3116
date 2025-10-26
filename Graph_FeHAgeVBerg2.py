import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import scipy.stats as stats
from scipy.stats import norm 
def outlier(df, lower_probability=0.65, upper_probability=0.9):
    slope, intercept, *_ = stats.linregress(df['FeH'], df['Age'])
    df['Predicted_Age'] = intercept + slope * df['FeH']
    df['Residual'] = df['Age'] - df['Predicted_Age']
    mu = st.mean(df['Residual'])
    std = np.std(df['Residual'])
    upprDvdingLine = norm.ppf(1-lower_probability, mu, std)
    lwrDvdLine = norm.ppf(upper_probability, mu, std)
    potentially_accreted_old = df[df['Residual'] > lwrDvdLine]
    potentially_accreted_young = df[df['Residual'] < upprDvdingLine]
    normal = df[(df['Residual'] <= lwrDvdLine) & (df['Residual'] >= upprDvdingLine)]

    print("mean residual:", round(mu, 3))
    print("standard deviation of residual:", round(std, 3))
    print("lower dividing line:", round(lwrDvdLine, 3))
    print("upper dividing line:", round(upprDvdingLine, 3))
    print("list of possible accreted clusters (younger than expected)")
    print(potentially_accreted_young[['NGC', 'Name', 'FeH', 'Age', 'Residual']])
    print("list of possible accreted clusters (older than expected)")
    print(potentially_accreted_old[['NGC', 'Name', 'FeH', 'Age', 'Residual']])
    return normal, potentially_accreted_young, potentially_accreted_old, slope, intercept, lwrDvdLine, upprDvdingLine

def starter():
    df = pd.read_csv('vandenBerg_table2.csv')
    print("Data Loaded:", len(df), "clusters")
    normal, potentially_accreted_young, potentially_accreted_old, slope, intercept, lwrDvdLine, upprDvdingLine = outlier(df, lower_probability=0.65)
    return normal, potentially_accreted_young, potentially_accreted_old, slope, intercept, df, lwrDvdLine, upprDvdingLine

normal, potentially_accreted_young, potentially_accreted_old, slope, intercept, df, lwrDvdLine, upprDvdingLine = starter()
plt.figure(figsize=(10, 6))
plt.errorbar(normal['Age'], normal['FeH'], xerr=normal['Age_err'], fmt='o', color='grey', alpha=0.6, label='Normal Clusters', capsize=2)
plt.errorbar(potentially_accreted_young['Age'], potentially_accreted_young['FeH'], xerr=potentially_accreted_young['Age_err'], fmt='o', color='red', alpha=0.8, label='Potentially Accreted (Younger)', capsize=2)
plt.errorbar(potentially_accreted_old['Age'], potentially_accreted_old['FeH'], xerr=potentially_accreted_old['Age_err'], fmt='o', color='blue', alpha=0.8, label='Potentially Accreted (Older)', capsize=2)


plt.xlabel('Age (Gyr)')
plt.ylabel('[Fe/H]')
plt.title('Globular Clusters Age vs [Fe/H] with Potentially Accreted Clusters')
plt.legend()
plt.tight_layout()
plt.gca()
plt.show()