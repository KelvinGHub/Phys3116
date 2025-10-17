#Test
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import scipy.stats as stats
from scipy.stats import norm 
from astropy.io import ascii
vandenberg = ascii.read("vandenBerg_table2.csv", format='basic', delimiter=',', guess=False)
krause21 = ascii.read("Krause21.csv", format='basic', delimiter=',', guess=False)
combined = ascii.join([vandenberg, krause21], keys=['Cluster name'], join_type='inner')
# Instead of print(joined.colnames)
for name in combined.colnames:
    print(repr(name))
