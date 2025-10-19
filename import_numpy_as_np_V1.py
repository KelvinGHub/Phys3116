import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import cmasher as cm
import re
import pandas as pd
import statistics as st
import scipy.stats as stats
from scipy.stats import norm 
from mpl_toolkits.mplot3d import Axes3D
import sys

def rest():
    column_names = ['ID', 'RA', 'DEC','L','B','R_Sun','R_gc','X','Y','Z',
                    'v_r', 'v_r_e', 'v_LSR', 'sig_v', 'sig_v_e', 'c', 'r_c', 'r_h', 'mu_V', 'rho_0', 'lg_tc', 'lg_th',
                    'Mstar','rh','C5','Age','FeH',
                    'FeH2','Age2','Age_err','HBtype','R_G','M_V','v_e0','log_sigma_0','accreted']
    amalgResult =  pd.DataFrame(index=range(150),columns=column_names)
    columns_to_fill = ['Age', 'FeH']
    amalgResult[columns_to_fill] = amalgResult[columns_to_fill].fillna(0)
    columns_to_fill = ['accreted']
    amalgResult[columns_to_fill] = amalgResult[columns_to_fill].fillna(-1)
    print('Converted NaN tp 0')
    amalgResult = amalgResult.astype({'FeH':float, 'Age':int})
    print('Changing data type')
    rowNum = 0
    Harris1 = pd.read_csv("HarrisPartI.csv")
    Harris3 = pd.read_csv("HarrisPartIII.csv")
    Krause = pd.read_csv("Krause21.csv")
    vanden = pd.read_csv("vandenBerg_table2.csv")
    Harris1.reset_index()
    Harris3.reset_index()
    Krause.reset_index()
    vanden.reset_index()
    #print(Harris1.loc[0:1,:])
    for index, row in Harris1.iterrows(): 
        #print(row)
        #print("Index = ",index)
        
        if Harris1.loc[index,'ID'].find("NGC") == -1: 
            continue
        amalgResult.loc[rowNum,'ID'] = Harris1.loc[index,'ID']
        amalgResult.loc[rowNum,'RA'] = Harris1.loc[index,'RA']
        amalgResult.loc[rowNum,'DEC'] = Harris1.loc[index,'DEC']
        amalgResult.loc[rowNum,'L'] = Harris1.loc[index,'L']
        amalgResult.loc[rowNum,'B'] = Harris1.loc[index,'B']
        amalgResult.loc[rowNum,'R_Sun'] =  Harris1.loc[index,'R_Sun']
        amalgResult.loc[rowNum,'R_gc'] = Harris1.loc[index,'R_gc']
        amalgResult.loc[rowNum,'X'] = Harris1.loc[index,'X']
        amalgResult.loc[rowNum,'Y'] = Harris1.loc[index,'Y']
        amalgResult.loc[rowNum,'Z'] = Harris1.loc[index,'Z']
        amalgResult.loc[rowNum,'v_r'] = Harris3.loc[index,'v_r']
        amalgResult.loc[rowNum,'v_r_e'] = Harris3.loc[index,'v_r_e']
        amalgResult.loc[rowNum,'v_LSR'] = Harris3.loc[index,'v_LSR']
        amalgResult.loc[rowNum,'sig_v'] = Harris3.loc[index,'sig_v']
        amalgResult.loc[rowNum,'sig_v_e'] = Harris3.loc[index,'sig_v_e']
        amalgResult.loc[rowNum,'c'] = Harris3.loc[index,'c']
        amalgResult.loc[rowNum,'r_c'] = Harris3.loc[index,'r_c']
        amalgResult.loc[rowNum,'r_h'] = Harris3.loc[index,'r_h']
        amalgResult.loc[rowNum,'mu_V'] = Harris3.loc[index,'mu_V']
        amalgResult.loc[rowNum,'rho_0'] = Harris3.loc[index,'rho_0']
        amalgResult.loc[rowNum,'lg_tc'] = Harris3.loc[index,'lg_tc']
        amalgResult.loc[rowNum,'lg_th'] = Harris3.loc[index,'lg_th']
        #print("Index = ",index)
        #print(Harris1.loc[rowNum,'ID'])
        # if Harris1.loc[rowNum,'ID'].find("NGC") == -1: 
        #     rowNum = rowNum + 1
        #     continue
        numbers_as_strings = re.findall(r'\d+', Harris1.loc[index,'ID'])
        a = [int(num) for num in numbers_as_strings]
        size_a = len(a)
        if size_a == 1:
            mask = "NGC" + "".join(numbers_as_strings)
            if mask == 'NGC6441': print('6441 found') 
            #print("mask",mask)
            krow = Krause.loc[Krause['Object'] == mask]
            #print(krow)
            #print(krow.iloc[0]['Mstar'])
            
            if len(krow) == 1:
                amalgResult.loc[rowNum,'Mstar'] = krow.iloc[0]['Mstar']
                amalgResult.loc[rowNum,'rh'] = krow.iloc[0]['rh']
                amalgResult.loc[rowNum,'C5'] = krow.iloc[0]['C5']
                amalgResult.loc[rowNum,'Age'] = krow.iloc[0]['Age']
                amalgResult.loc[rowNum,'FeH'] = krow.iloc[0]['FeH']
                Krause = Krause.drop(krow.index)
                
                #print("krow found")
            else:
                #print(mask, "krow not found")
                continue    
            vrow = vanden.loc[vanden['#NGC'] == "".join(numbers_as_strings)]
            if len(vrow) == 1:
                amalgResult.loc[rowNum,'FeH2'] = vrow.iloc[0]['FeH']
                amalgResult.loc[rowNum,'Age2'] = vrow.iloc[0]['Age']
                amalgResult.loc[rowNum,'Age_err'] = vrow.iloc[0]['HBtype']
                amalgResult.loc[rowNum,'R_G'] = vrow.iloc[0]['R_G']
                amalgResult.loc[rowNum,'M_V'] = vrow.iloc[0]['M_V']
                amalgResult.loc[rowNum,'v_e0'] = vrow.iloc[0]['v_e0']
                amalgResult.loc[rowNum,'log_sigma_0'] = vrow.iloc[0]['log_sigma_0']
                #print("vrow found")
            else:
                rowNum = rowNum + 1
                continue
            #     print("".join(numbers_as_strings), "vrow not found")
    
    #    amalgResult.loc[rowNum,'FeH2'] = vanden.loc[rowNum,'FeH']
    #    amalgResult.loc[rowNum,'Age2'] = vanden.loc[rowNum,'Age']
    #    amalgResult.loc[rowNum,'Age_err'] = vanden.loc[rowNum,'Age_err']
    #    amalgResult.loc[rowNum,'HB_type'] = vanden.loc[rowNum,'HB_type']
    #    amalgResult.loc[rowNum,'R_G'] = vanden.loc[rowNum,'R_G']
    #    amalgResult.loc[rowNum,'M_V'] = vanden.loc[rowNum,'M_V']
    #    amalgResult.loc[rowNum,'v_e0'] = vanden.loc[rowNum,'v_e0']
    #    amalgResult.loc[rowNum,'log_sigma_0'] = vanden.loc[rowNum,'log_sigma_0']
        rowNum = rowNum + 1 
        # if rowNum > 2: 
        #     break
    for index2, krow in Krause.iterrows():
        #print (krow.loc['Object'])
        amalgResult.loc[rowNum,'Mstar'] = krow.loc['Mstar']
        amalgResult.loc[rowNum,'rh'] = krow.loc['rh']
        amalgResult.loc[rowNum,'C5'] = krow.loc['C5']
        amalgResult.loc[rowNum,'Age'] = krow.loc['Age']
        amalgResult.loc[rowNum,'FeH'] = krow.loc['FeH']
        rowNum = rowNum + 1    
    print("Number of rows joined", rowNum, amalgResult.loc[0,"FeH"].dtype)
    amalgResult = amalgResult.dropna(subset=['ID'])
    #print(amalgResult.loc[0:20,:])
    #print(amalgResult.loc[33:49,:])
    #print(Krause['FeH'].dtype, amalgResult['FeH'].dtype)        
    #slope, intercept, *_ = stats.linregress(Krause['FeH'], Krause['Age'])
    print(Krause)
    slope, intercept, *_ = stats.linregress(amalgResult['FeH'], amalgResult['Age'])
    starter(amalgResult) 
    #outliers(amalgResult)
    #amalgResult[0]['ID'] = Harris1[0]['ID']
    #print(amalgResult[0]['ID'])
    return amalgResult

    # Initialize NGC number (column 0)
def ThreeDPlot(df):
    print('3D test')
    x_data = df['X']
    y_data = df['Y']
    z_data = df['Z']
    # num_points = 100
    # x_data = np.random.rand(num_points) * 10
    # y_data = np.random.rand(num_points) * 10
    # z_data = np.random.rand(num_points) * 10
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Scatter Plot of Coordinates')
    ax.scatter(x_data, y_data, z_data, c='black', marker='o')
    colors = [0,1] # Values to determine color
    color_map = {1: 'red', 0: 'green'}
    colors = df['accreted']
    print("colors\n", df.loc[df['accreted'] == 1])
    ax.scatter3D(x_data, y_data, z_data, c=colors, cmap='viridis') # 'viridis' is a common colormap
    #plt.colorbar(ax.scatter3D(x_data, y_data, z_data, c=colors, cmap='viridis'), ax=ax, shrink=0.5, aspect=5)
    plt.colorbar(ax.scatter3D(x_data, y_data, z_data, c=colors), ax=ax, shrink=0.5, aspect=5)
    print("test 3d plot")
    plt.show()
    print("end test 3d plot")
    return
def indicateAccretion(df, accreted):
        selected_rows = df[df['ID'].isin(accreted['ID'])]
        selected_rows.loc['accreyed'] = 1 
        print('selected rows in indi\n',selected_rows) 
def outliers(df):
    print("Before reading")
    # df = pd.read_csv('Krause21.csv')
    print("Data Loaded:", len(df), "clusters")
    normal, accreted, other_outliers, slope, intercept, lwrDvdLine, upprDvdingLine = outlier(0.95, df)
    #print("colors 2\n", df.loc[df['accreted'] == 1])
    return normal, accreted, other_outliers, slope, intercept, df, lwrDvdLine, upprDvdingLine
def starter(df):
    normal, accreted, other_outliers, slope, intercept, df, lwrDvdLine, upprDvdingLine = outliers(df)
    #print("accreted 3\n", df.loc[df['accreted'] == 1])
    plt.figure(figsize=(10, 6))
    plt.scatter(normal['FeH'], normal['Age'], color='grey', label='Normal Clusters')
    plt.scatter(accreted['FeH'], accreted['Age'], color='red', label='Accreted Clusters')
    plt.scatter(other_outliers['FeH'], other_outliers['Age'], color='orange', label='Other Outliers')
    x_vals = np.linspace(df['FeH'].min(), df['FeH'].max(), 100)
    plt.plot(x_vals, intercept + slope * x_vals, color='black', linestyle='--', label='Regression Line')
    # Plot upper and lower dividing lines
    plt.plot(x_vals, intercept + slope * x_vals + upprDvdingLine, color='blue', linestyle=':', label='Upper Dividing Line')
    plt.plot(x_vals, intercept + slope * x_vals + lwrDvdLine, color='green', linestyle=':', label='Lower Dividing Line')
    for _, row in accreted.iterrows():
        plt.text(row['FeH']+0.03, row['Age'], 'Accreted', fontsize=9, color='red', weight='bold')
    for _, row in other_outliers.iterrows():
        plt.text(row['FeH']+0.03, row['Age'], 'Outlier', fontsize=9, color='orange', weight='bold')

    plt.xlabel('[Fe/H]')
    plt.ylabel('Age (Gyr)')
    plt.title('Globular Clusters Age vs [Fe/H] with Outliers')
    plt.legend()
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.show()
def outlier(probability, df):
    print("start of outlier routine", df['FeH'].dtype)
    slope, intercept, *_ = stats.linregress(df['FeH'], df['Age'])
    df['Predicted_Age'] = intercept + slope * df['FeH']
    df['Residual'] = df['Age'] - df['Predicted_Age']
    mu = st.mean(df['Residual'])
    std = np.std(df['Residual'])
    if probability > 0.5:
        upprDvdingLine = norm.ppf(probability, mu, std)
        lwrDvdLine = norm.ppf(1 - probability, mu, std)
    else:
        upprDvdingLine = norm.ppf(1 - probability, mu, std)
        lwrDvdLine = norm.ppf(probability, mu, std)
    accreted = df[df['Residual'] < lwrDvdLine]
    for index, row in df.iterrows():
        if (accreted['ID'] == row['ID']).any():
            #if row['ID'].isin(accreted['ID']):
            df.loc[index,'accreted'] = 1
            #print('Then\n',df.loc[index,'accreted'])
    # df0.loc[:,'accreted'] = 1 
    #selected_rows.loc['accreyed'] = 1 
    #indicateAccretion(df, accreted)
    #df2 = df.loc[df['accreted'] == 1]
    #print('df0\n',df0.loc[:,'accreted'])
    selected_columns = df[['ID','X', 'Y','Z', 'accreted']]
    #selected_columns2 = df0[['ID','X', 'Y','Z', 'accreted']]
    # print('Then\n',selected_columns2)
    #print('x, y, z of 4 rows\n', selected_columns)
    
    # print("after indi\n", df2)
    other_outliers = df[df['Residual'] > upprDvdingLine]
    normal = df[(df['Residual'] >= lwrDvdLine) & (df['Residual'] <= upprDvdingLine)]

    print("mean residual:", round(mu, 3))
    print("standard deviation of residual:", round(std, 3))
    print("lower dividing line:", round(lwrDvdLine, 3))
    print("upper dividing line:", round(upprDvdingLine, 3))
    print("list of possible accreted clusters")
    print(accreted[['ID', 'FeH', 'Age', 'Residual']])
    #print(accreted[['Object', 'AltName', 'FeH', 'Age', 'Residual']])

    return normal, accreted, other_outliers, slope, intercept, lwrDvdLine, upprDvdingLine




amalgaResult = rest()
ThreeDPlot(amalgaResult)

 
