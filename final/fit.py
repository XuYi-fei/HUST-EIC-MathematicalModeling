import pandas as pd
import os
import numpy as np

data = pd.read_excel('Preprocessed_original.xlsx', sheet_name='Sheet1')
columns = list(data.columns)
writer = pd.ExcelWriter('Preprocessed.xlsx', engine='xlsxwriter')
data0 = pd.read_excel('Preprocessed.xlsx', sheet_name='original_data')
data1 = pd.read_excel('Preprocessed.xlsx', sheet_name='SD')
data2 = pd.read_excel('Preprocessed.xlsx', sheet_name='CT')
data3 = pd.read_excel('Preprocessed.xlsx', sheet_name='DS')
data4 = pd.read_excel('Preprocessed.xlsx', sheet_name='PR')
countries = {i:0 for i in data.values[:, 0]}


for index, row in data.iterrows():
    Q = np.array(row[3:], dtype=np.float64)
    t = np.array(range(len(row[3:])), dtype=np.float64)

    model = np.polyfit(t, Q, deg=1)
    countries[row[0]] = model
output = {'Country/Region':list(countries.keys()), 'a':[i[0] for i in countries.values()], 'b':[i[1] for i in countries.values()]}
data2 = pd.DataFrame(output)
data0.to_excel(writer, sheet_name='original_data')
data1.to_excel(writer, sheet_name='SD')
data2.to_excel(writer, sheet_name='CT')
data3.to_excel(writer, sheet_name='DS')
data4.to_excel(writer, sheet_name='PR')
writer.save()
writer.close()