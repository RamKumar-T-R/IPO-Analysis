# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 21:27:04 2024

@author: Ramkumar
"""

# Importing the required libraries
import pandas as pd
import numpy as np

# Importing the dataset
file_path = "D:/ML_projects/IPO_analysis/Dataset/mainboard-ipo-list-in-india-bse-nse2023.csv"
temp_file_path = "D:/ML_projects/IPO_analysis/Temp/mainboard-ipo-tickers-list-in-india-bse-nse2023.csv"
dataset = pd.read_csv(file_path)

# function for retriving tiker from google search
from googlesearch import search
def name_to_id(self):
    
    searchval = 'yahoo finance '+self
    link = []
    #limits to the first link
    for url in search(searchval, lang='es', sleep_interval=10):  # sleep_interval=2
        link.append(url)

    link = str(link[0])
    link=link.split("/")
    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]

    return(ticker)

# Retriving tickers
tickers = []
for i in dataset.iloc[32:, 0]:
    ticker = name_to_id(i)
    tickers.append(ticker)
    print(ticker, len(tickers))
    temp_df = pd.DataFrame({'Tickers': tickers})
    temp_df.to_csv(temp_file_path)

# Concatinating with existing dataframe
#new_data_frame = pd.concat([dataset, pd.DataFrame({'Tickers': tickers})], axis=1)

# Exporting the DataFrame to csv_file
#new_data_frame.to_csv(file_path)