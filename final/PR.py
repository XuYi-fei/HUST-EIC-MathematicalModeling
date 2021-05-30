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
data2 = pd.read_excel('Preprocessed.xlsx', sheet_name='CT')
data3 = pd.read_excel('Preprocessed.xlsx', sheet_name='DS')

countries = {i:0 for i in data.values[:, 0]}
Qs = []
for index, row in data.iterrows():
    Q = np.array(row[3:], dtype=np.float64)
    Qs.append(np.sum(Q))

Qmin = np.min(Qs)
Qmax = np.max(Qs)
for index, row in data.iterrows():
    Q = np.array(row[3:], dtype=np.float64)
    result = (np.sum(Q) - Qmin) / (Qmax - Qmin)
    countries[row[0]] = result
print(Qmin, Qmax)
output = {'Country/Region':list(countries.keys()), 'PR':list(countries.values())}
data4 = pd.DataFrame(output)

data0.to_excel(writer, sheet_name='original_data')
data1.to_excel(writer, sheet_name='SD')
data2.to_excel(writer, sheet_name='CT')
data3.to_excel(writer, sheet_name='DS')
data4.to_excel(writer, sheet_name='PR')
writer.save()
writer.close()