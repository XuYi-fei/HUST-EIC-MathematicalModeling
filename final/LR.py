from functools import reduce
from numpy.core.defchararray import title
from numpy.core.fromnumeric import mean, sort
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
data4 = pd.read_excel('Preprocessed.xlsx', sheet_name='PR')

countries = {i:0 for i in data.values[:, 0]}
Qs = []
for index, row in data.iterrows():
    Q = list(row[3:])
    Q = sorted(Q)
    avg = mean(Q)
    length = len(Q)
    medium = Q[(length-1)//2]
    up_quarter = Q[(length-1)//4 * 3]
    down_quarter = Q[(length-1)//4]
    
    abnormal_up_quater = 1.5 * up_quarter
    abnormal_down_quater = 1.5 * down_quarter
    # tmp = np.array(Q) > abnormal_up_quater
    abnormals = (np.array(Q) > abnormal_up_quater).sum() + (np.array(Q) < abnormal_down_quater).sum()
    
    
        
    countries[row[0]] = [down_quarter, medium, up_quarter, avg, abnormals]
output = {'Country/Region':list(countries.keys()), '下四分位点':[i[0] for i in countries.values()],
          '中位数':[i[1] for i in countries.values()],'上四分位点':[i[2] for i in countries.values()],
          '均值':[i[3] for i in countries.values()], '异常数目':[i[4] for i in countries.values()]}
data5 = pd.DataFrame(output)

data0.to_excel(writer, sheet_name='original_data')
data1.to_excel(writer, sheet_name='SD')
data2.to_excel(writer, sheet_name='CT')
data3.to_excel(writer, sheet_name='DS')
data4.to_excel(writer, sheet_name='PR')
data5.to_excel(writer, sheet_name='LR')
writer.save()
writer.close()