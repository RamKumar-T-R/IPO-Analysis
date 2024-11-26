# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:49:31 2024

@author: Ramkumar
"""

# Importing the increased dates

import yfinance as yf
import pandas as pd
from datetime import date

cmp_id = 'PRINCEPIPE.NS'
dateNames = ['IPO Issue', 'Initial-Openning', '50%-increased', '100%-increased', '150%-increased', '200%-increased', 'Current']
dates = []

# Importing the dataset
list_data = pd.read_csv("D:/ML_projects/IPO_analysis/Dataset/mainboard-ipo-list-in-india-bse-nse2019.csv")

# Month dictionary
month_to_num = {'Jan': 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


            
            
def linear_search(cmp_price_data, price):
    if(cmp_price_data.iloc[cmp_price_data.shape[0]-1, :]['Close'] < price):
        print('The expected growth is not yet met')
        return date(1, 1, 1)   # Dummy date
    
    for i in range(cmp_price_data.shape[0]):
        if(cmp_price_data.iloc[i, 3] >= price):
            return cmp_price_data.iloc[i, :].name.date()
        
    

# Full price data - daywise
cmp_price_data = yf.Ticker(cmp_id).history(period='max', interval='1d')


# Prices

# IPO issue price
cmp_ipo_price = list_data.loc[list_data['Tickers'] == cmp_id].iloc[:, 4][0]

# Openning price
cmp_init_price = cmp_price_data.iloc[0, 3]

# 50% increased price
cmp_50percent_price = cmp_init_price + (cmp_init_price * 0.5)

# 100% increased price
cmp_100percent_price = cmp_init_price + (cmp_init_price * 1)

# 150% increased price
cmp_150percent_price = cmp_init_price + (cmp_init_price * 1.5)

# 200% increased price
cmp_200percent_price = cmp_init_price + (cmp_init_price * 2)

# Current price
cmp_curr_price = cmp_price_data.iloc[cmp_price_data.shape[0]-1, 3]


# Dates 

# Ipo release date
cmp_ipo_date = date(int(list_data.loc[list_data['Tickers'] == cmp_id].iloc[:, 3][0][8: 12]), month_to_num[list_data.loc[list_data['Tickers'] == cmp_id].iloc[:, 3][0][0: 3]], int(list_data.loc[list_data['Tickers'] == cmp_id].iloc[:, 3][0][4: 6]))
dates.append(cmp_ipo_date)

# initial date
cmp_init_date = cmp_price_data.iloc[0, :].name.date()
dates.append(cmp_init_date)

# 50 increased date
cmp_50percent_date = linear_search(cmp_price_data, cmp_50percent_price)
dates.append(cmp_50percent_date)

# 100 increased date
cmp_100percent_date = linear_search(cmp_price_data, cmp_100percent_price)
dates.append(cmp_100percent_date)

# 150 increased date
cmp_150percent_date = linear_search(cmp_price_data, cmp_150percent_price)
dates.append(cmp_150percent_date)

# 200 increased date
cmp_200percent_date = linear_search(cmp_price_data, cmp_200percent_price)
dates.append(cmp_200percent_date)

# Current date
cmp_curr_date = cmp_price_data.iloc[cmp_price_data.shape[0]-1, :].name.date()
dates.append(cmp_curr_date)


# Converting date_list o dataFrame
dateDict = {'Date Names': dateNames, 'Dates': dates}
dateDF = pd.DataFrame(dateDict)
dateDF = dateDF.reset_index()