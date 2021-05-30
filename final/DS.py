from functools import reduce
from numpy.core.defchararray import title
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('Preprocessed_original.xlsx', sheet_name='Sheet1')
columns = list(data.columns)
writer = pd.ExcelWriter('Preprocessed.xlsx', engine='xlsxwriter')
data0 = pd.read_excel('Preprocessed.xlsx', sheet_name='original_data')
data1 = pd.read_excel('Preprocessed.xlsx', sheet_name='SD')
data2 = pd.read_excel('Preprocessed.xlsx', sheet_name='回归系数')

countries = {i:0 for i in data.values[:, 0]}
for index, row in data.iterrows():
    Q = np.array(row[3:], dtype=np.float64)
    result = [abs(Q[i] - Q[i-1]) for i in range(1, len(Q))]
    if row[0] == 'US':
        t = list(range(len(result)))
        plt.title("US confirmed people")
        plt.plot(t[40:100], result[40:100], color='red',label="After diffrential")
        plt.plot(t[41:100], Q[41:100], color='blue', label='Original')
        plt.legend()
        plt.show()
        
#     countries[row[0]] = result
# output = {'Country/Region':list(countries.keys()), 'DS':list(countries.values())}
# data3 = pd.DataFrame(output)

# data0.to_excel(writer, sheet_name='original_data')
# data1.to_excel(writer, sheet_name='SD')
# data2.to_excel(writer, sheet_name='回归系数')
# data3.to_excel(writer, sheet_name='DS')
# writer.save()
# writer.close()