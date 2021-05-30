import pandas as pd
import os
import numpy as np

data = pd.read_excel('Preprocessed_original.xlsx')
columns = list(data.columns)
writer = pd.ExcelWriter('Preprocessed.xlsx', engine='xlsxwriter')
countries = {i:0 for i in data.values[:, 0]}


for index, row in data.iterrows():
    mean = np.mean(row[3:])
    n = len(row[3:])
    up = sum([(i-mean)**2 for i in row[3:]])
    countries[row[0]] = np.sqrt(up/(n-1))
output = {'Country/Region':list(countries.keys()), 'SD':list(countries.values())}
data2 = pd.DataFrame(output)
data2.to_excel(writer, sheet_name='SD')
data.to_excel(writer, sheet_name='original data')
writer.save()
writer.close()