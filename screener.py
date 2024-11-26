# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:59:38 2024

@author: Ramkumar
"""

# Importing the required files
import yfinance as yf
import pandas as pd
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from time import sleep

# File path
file_path = "D:/ML_projects/IPO_analysis/Screeners/mainboard-ipo-cmps-screner-data-india-bse-nse2019.xlsm"
# Importing the dataset
list_data = pd.read_csv("D:/ML_projects/IPO_analysis/Dataset/mainboard-ipo-list-in-india-bse-nse2019.csv")
list_data.head()

# Month dictionary
month_to_num = {'Jan': 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


            
            
def linear_search(cmp_price_data, price):
    if(cmp_price_data.iloc[cmp_price_data.shape[0]-1, :]['Close'] < price):
        print('The expected growth is not yet met')
        return date(1, 1, 1)   # Dummy date
    
    for i in range(cmp_price_data.shape[0]):
        if(cmp_price_data.iloc[i, 3] >= price):
            return cmp_price_data.iloc[i, :].name.date()
        
            
# Data in lists
cmp_names = []
cmp_ids = list(list_data.iloc[:, 8])

cmp_ipo_prices = []
cmp_init_prices = []
cmp_50percent_prices = []
cmp_100percent_prices = []
cmp_150percent_prices = []
cmp_200percent_prices = []
cmp_curr_prices = []

cmp_ipo_dates = []
cmp_init_dates = []
cmp_50percent_dates = []
cmp_100percent_dates = []
cmp_150percent_dates = []
cmp_200percent_dates = []
cmp_curr_dates = []

cmp_diffs_ipo_init = []
cmp_diffs_init_50percent = []
cmp_diffs_init_100percent = []
cmp_diffs_init_150percent = []
cmp_diffs_init_200percent = []
cmp_diffs_init_curr = []

cmp_diffs_50percent_100percent = []
cmp_diffs_100percent_150percent = []
cmp_diffs_150percent_200percent = []
cmp_diffs_200percent_curr = []

infos = []
    

# Iterating each companies
for i in list_data.iloc[:, :].values:
    
    
    cmp_id = i[8]
    cmp_names.append(i[1][:len(i[1]) - 4])
    
    infos.append(yf.Ticker(cmp_id).info)
    
    # Full price data - daywise
    cmp_price_data = yf.Ticker(cmp_id).history(period='max', interval='1d')
    
    
    # Prices
    
    # IPO issue price
    cmp_ipo_price = i[4]
    cmp_ipo_prices.append(cmp_ipo_price) # Appending
    
    # Openning price
    cmp_init_price = cmp_price_data.iloc[0, 3]
    cmp_init_prices.append(cmp_init_price) # Appending
    
    # 50% increased price
    cmp_50percent_price = cmp_init_price + (cmp_init_price * 0.5)
    cmp_50percent_prices.append(cmp_50percent_price) # Appending
    
    # 100% increased price
    cmp_100percent_price = cmp_init_price + (cmp_init_price * 1)
    cmp_100percent_prices.append(cmp_100percent_price) # Appending
    
    # 150% increased price
    cmp_150percent_price = cmp_init_price + (cmp_init_price * 1.5)
    cmp_150percent_prices.append(cmp_150percent_price) # Appending
    
    # 200% increased price
    cmp_200percent_price = cmp_init_price + (cmp_init_price * 2)
    cmp_200percent_prices.append(cmp_200percent_price) # Appending
    
    # Current price
    cmp_curr_price = cmp_price_data.iloc[cmp_price_data.shape[0]-1, 3]
    cmp_curr_prices.append(cmp_curr_price) # Appending
    
    
    # Dates 
    
    # Ipo release date
    cmp_ipo_date = date(int(i[3][8: 12]), month_to_num[i[3][0: 3]], int(i[3][4: 6]))
    cmp_ipo_dates.append(cmp_ipo_date) # Appending
    
    # initial date
    cmp_init_date = cmp_price_data.iloc[0, :].name.date()
    cmp_init_dates.append(cmp_init_date) # Appending
    
    # 50 increased date
    cmp_50percent_date = linear_search(cmp_price_data, cmp_50percent_price)
    cmp_50percent_dates.append(cmp_50percent_date) # Appending
    
    # 100 increased date
    cmp_100percent_date = linear_search(cmp_price_data, cmp_100percent_price)
    cmp_100percent_dates.append(cmp_100percent_date) # Appeding
    
    # 150 increased date
    cmp_150percent_date = linear_search(cmp_price_data, cmp_150percent_price)
    cmp_150percent_dates.append(cmp_150percent_date) # Appending
    
    # 200 increased date
    cmp_200percent_date = linear_search(cmp_price_data, cmp_200percent_price)
    cmp_200percent_dates.append(cmp_200percent_date) # Appending
    
    # Current date
    cmp_curr_date = cmp_price_data.iloc[cmp_price_data.shape[0]-1, :].name.date()
    cmp_curr_dates.append(cmp_curr_date) # Appending
    
    
    
    # Selective Gap differences
    
    # IPO to Public Issuing date
    cmp_diff_ipo_init = cmp_init_date - cmp_ipo_date 
    cmp_diffs_ipo_init.append(cmp_diff_ipo_init)
    
    # Public Issuing to 50%
    cmp_diff_init_50percent = cmp_50percent_date - cmp_init_date
    cmp_diffs_init_50percent.append(cmp_diff_init_50percent) # Appending
    
    # Public Issuing to 100%
    cmp_diff_init_100percent = cmp_100percent_date - cmp_init_date
    cmp_diffs_init_100percent.append(cmp_diff_init_100percent) # Appending

    # Public Issuing to 150%
    cmp_diff_init_150percent = cmp_150percent_date - cmp_init_date
    cmp_diffs_init_150percent.append(cmp_diff_init_150percent) # Appending

    # Public Issuing to 200%
    cmp_diff_init_200percent = cmp_200percent_date - cmp_init_date
    cmp_diffs_init_200percent.append(cmp_diff_init_200percent) # Appending
    
    
    # Public Issuing to current_date
    cmp_diff_init_curr = cmp_curr_date - cmp_init_date
    cmp_diffs_init_curr.append(cmp_diff_init_curr) # Appending
    
    # 50% to 100%
    cmp_diff_50percent_100percent = cmp_50percent_date - cmp_init_date
    cmp_diffs_50percent_100percent.append(cmp_diff_50percent_100percent) # Appending
    
    # 100% to 150%
    cmp_diff_100percent_150percent = cmp_150percent_date - cmp_100percent_date
    cmp_diffs_100percent_150percent.append(cmp_diff_100percent_150percent) # Appending
    
    # 150% to 200%
    cmp_diff_150percent_200percent = cmp_200percent_date - cmp_150percent_date
    cmp_diffs_150percent_200percent.append(cmp_diff_150percent_200percent) # Appending
    
    # 200% to current_date
    cmp_diff_200percent_curr = cmp_curr_date - cmp_200percent_date
    cmp_diffs_200percent_curr.append(cmp_diff_200percent_curr) # Appending
    

# Converting data of 25 list to a dataframe
cmp_price_date_diff_dataframe = pd.DataFrame({
        'cmp_name': cmp_names, 
        'cmp_id': cmp_ids, 
        'cmp_ipo_price': cmp_ipo_prices, 
        'cmp_init_price': cmp_init_prices, 
        'cmp_50percent_price': cmp_50percent_prices,
        'cmp_100percent_price': cmp_100percent_prices,
        'cmp_150percent_price': cmp_150percent_prices,
        'cmp_200percent_price': cmp_200percent_prices,
        'cmp_curr_price': cmp_curr_prices,
        
        'cmp_ipo_date': cmp_ipo_dates,
        'cmp_init_date': cmp_init_dates,
        'cmp_50percent_date': cmp_50percent_dates,
        'cmp_100percent_date': cmp_100percent_dates,
        'cmp_150percent_date': cmp_150percent_dates,
        'cmp_200percent_date': cmp_200percent_dates,
        'cmp_curr_date': cmp_curr_dates,
        
        'cmp_diff_ipo_init': cmp_diffs_ipo_init,
        'cmp_diff_init_50percent': cmp_diffs_init_50percent,
        'cmp_diff_init_100percent': cmp_diffs_init_100percent,
        'cmp_diff_init_150percent': cmp_diffs_init_150percent,
        'cmp_diff_init_200percent': cmp_diffs_init_200percent,
        'cmp_diff_init_curr': cmp_diffs_init_curr,
        
        'cmp_diff_50percent_100percent': cmp_diffs_50percent_100percent,
        'cmp_diff_100percent_150percent': cmp_diffs_100percent_150percent,
        'cmp_diff_150percent_200percent': cmp_diffs_150percent_200percent,
        'cmp_diff_200percent_curr': cmp_diffs_200percent_curr
    })

# Exporging the dataframe to csv file
cmp_price_date_diff_dataframe.to_excel(file_path)