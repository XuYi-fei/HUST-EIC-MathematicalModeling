import pandas as pd
import os
import csv

data = pd.read_csv(r"D:\GitRepos\EIC\MathmaticalModeling\HUST-EIC-MathematicalModeling\final\time_series_covid_19_confirmed.csv")
columns = dict(zip(range(len(data.columns)), data.columns))
columnIndex = list(data.columns)[1:]
countries = {}
for index, row in data.iterrows():
    if row[1] not in countries.keys():
        # import pdb; pdb.set_trace()
        countries[row[1]] = {}
        countries[row[1]][columns[2]] = row[2]
        countries[row[1]][columns[3]] =row[3]
        for j in range(4, len(columns)):
            countries[row[1]][columns[j]] = 0
    for j in range(5, len(columns)):
        countries[row[1]][columns[j]] += (row[j] - row[j-1])

writer_columns = {}
for index in columnIndex:
    if index == 'Country/Region':
        writer_columns[index] = list(countries.keys())
    else:
        writer_columns[index] = [i[index] for i in countries.values()]
dataFrame = pd.DataFrame(writer_columns)
dataFrame.to_excel('Preprocessed_original.xlsx')



    
         