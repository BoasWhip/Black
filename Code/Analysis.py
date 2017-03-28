# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:08:10 2017
@author: ozsanos
"""

import pandas as pd

raw_data = pd.read_csv('data.csv')
raw_columns = list(raw_data)

columns = set()
dates = list()

"""
    Delete raw columns
"""
for column in raw_columns:
    if column[0:8] == "Unnamed:":
        del raw_data[column]
    else:
        columns.add(column.split(" ")[0])

"""
    Compile unique dates
"""
raw_columns = list(raw_data)


for column in raw_columns:
    print(raw_data[0,column])

  

print(raw_data)
print(columns)
