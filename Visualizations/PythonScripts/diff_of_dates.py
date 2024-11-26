# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:52:48 2024

@author: Ramkumar
"""

# Importing the DatesBetween

import yfinance as yf
import pandas as pd
from datetime import date

cmp_id = 'PRINCEPIPE.NS'
diff_names = ['IPO-InitialOpenning', 'InitialOpenning-50%', 'InitialOpenning-100%', 'InitialOpenning-150%', 'InitialOpenning-200%', 'InitialOpenning-Current', '50%-100%', '100%-150%', '150%-200%', '200%-Current']
diffs = []


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

# initial date
cmp_init_date = cmp_price_data.iloc[0, :].name.date()

# 50 increased date
cmp_50percent_date = linear_search(cmp_price_data, cmp_50percent_price)

# 100 increased date
cmp_100percent_date = linear_search(cmp_price_data, cmp_100percent_price)

# 150 increased date
cmp_150percent_date = linear_search(cmp_price_data, cmp_150percent_price)

# 200 increased date
cmp_200percent_date = linear_search(cmp_price_data, cmp_200percent_price)

# Current date
cmp_curr_date = cmp_price_data.iloc[cmp_price_data.shape[0]-1, :].name.date()



# Selective Gap differences

# IPO to Public Issuing date
cmp_diff_ipo_init = cmp_init_date - cmp_ipo_date 
diffs.append(cmp_diff_ipo_init)

# Public Issuing to 50%
cmp_diff_init_50percent = cmp_50percent_date - cmp_init_date
diffs.append(cmp_diff_init_50percent)

# Public Issuing to 100%
cmp_diff_init_100percent = cmp_100percent_date - cmp_init_date
diffs.append(cmp_diff_init_100percent)

# Public Issuing to 150%
cmp_diff_init_150percent = cmp_150percent_date - cmp_init_date
diffs.append(cmp_diff_init_150percent)

# Public Issuing to 200%
cmp_diff_init_200percent = cmp_200percent_date - cmp_init_date
diffs.append(cmp_diff_init_200percent)

# Public Issuing to current_date
cmp_diff_init_curr = cmp_curr_date - cmp_init_date
diffs.append(cmp_diff_init_curr)


# 50% to 100%
cmp_diff_50percent_100percent = cmp_50percent_date - cmp_init_date
diffs.append(cmp_diff_50percent_100percent)

# 100% to 150%
cmp_diff_100percent_150percent = cmp_150percent_date - cmp_100percent_date
diffs.append(cmp_diff_100percent_150percent)

# 150% to 200%
cmp_diff_150percent_200percent = cmp_200percent_date - cmp_150percent_date
diffs.append(cmp_diff_150percent_200percent)

# 200% to current_date
cmp_diff_200percent_curr = cmp_curr_date - cmp_200percent_date
diffs.append(cmp_diff_200percent_curr)


# Creating the dataFrame
diffDict = {'Difference Between': diff_names, 'Duration': diffs}
diffDF = pd.DataFrame(diffDict).reset_index()


