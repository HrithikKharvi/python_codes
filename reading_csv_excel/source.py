# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:53:29 2023

@author: admin
"""

import pandas as pd
import datetime

file_path = r"D:\python_commits\reading_csv_excel_pandas"
file_name = "\sample_data.csv"


if ".csv" in file_name:
    df = pd.read_csv(file_path + file_name)
else:
    df = pd.read_csv(file_path + file_name)


#adding new column into the dataframe and saving the file 
df["date"] = datetime.datetime.now()

df.to_csv("result.csv", index=False)
