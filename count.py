import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.read_excel('/Users/kelvinchen/Downloads/Book1.xlsx')
all_values = pd.concat([df[col] for col in df.columns], ignore_index=True)
all_values = all_values.dropna()
all_values = all_values.astype(str)
value_counts = all_values.value_counts()
unique_once = value_counts[value_counts == 1]
unique_once_sorted = unique_once.sort_index()
print("=== Frequency of each cluster across all columns ===")
print(unique_once_sorted)
print("=== Total number of unique clusters that appear only once ===")
print(len(unique_once_sorted))