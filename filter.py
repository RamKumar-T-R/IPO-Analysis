# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 19:25:34 2023

@author: Ramkumar
"""

# Importing the required files
import yfinance as yf
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Reading the data
from time import sleep
list_data = pd.read_csv("D:/ML_projects/IPO_analysis/Dataset/mainboard-ipo-list-in-india-bse-nse2019.csv")
list_data.head()

# Month dictionary
month_to_num = {'Jan': 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

# Filtered companies list
good_cmp_ids = []

for i in list_data.iloc[:, :].values:
    print(i[1][: len(i[1])-4], "     ", "Prices", "     ", "Growth percent")
    cmp_id = i[8]
       
    # Full price data - daywise
    cmp_price_data = yf.Ticker(cmp_id).history(period='max', interval='1d')
      
    # dates
    cmp_init_date = cmp_price_data.iloc[0, :].name.date()
    cmp_3mo_date = cmp_init_date + relativedelta(months=3)
    cmp_6mo_date =  cmp_init_date + relativedelta(months=6)
    cmp_12mo_date = cmp_init_date + relativedelta(months=12)
    cmp_18mo_date = cmp_init_date + relativedelta(months=18)
        
    # Prices
    cmp_init_price = yf.Ticker(cmp_id).history(start = str(cmp_init_date), end = str(cmp_init_date+relativedelta(days=15)), interval="1d").values[0][3]  # obtaining the close value of that day
    cmp_3mo_price = yf.Ticker(cmp_id).history(start = str(cmp_3mo_date), end = str(cmp_3mo_date+relativedelta(days=15)), interval="1d").values[0][3]  # obtaining the close value of that day
    cmp_6mo_price = yf.Ticker(cmp_id).history(start = str(cmp_6mo_date), end = str(cmp_6mo_date+relativedelta(days=15)), interval="1d").values[0][3]  # obtaining the close value of that day
    cmp_12mo_price = yf.Ticker(cmp_id).history(start = str(cmp_12mo_date), end = str(cmp_12mo_date+relativedelta(days=15)), interval="1d").values[0][3]  # obtaining the close value of that day
    cmp_18mo_price = yf.Ticker(cmp_id).history(start = str(cmp_18mo_date), end = str(cmp_18mo_date+relativedelta(days=15)), interval="1d").values[0][3]  # obtaining the close value of that day
        
    # Percents
       
    cmp_3mo_gp = (cmp_3mo_price - cmp_init_price) / cmp_init_price
    cmp_6mo_gp = (cmp_6mo_price - cmp_init_price) / cmp_init_price
    cmp_12mo_gp = (cmp_12mo_price - cmp_init_price) / cmp_init_price
    cmp_18mo_gp = (cmp_18mo_price - cmp_init_price) / cmp_init_price
        
    # Printing
    print('Initital', "          ", cmp_init_price)
    print('3 Month', "          ", cmp_3mo_price, "      ", cmp_3mo_gp)
    print('6 Month', "          ", cmp_6mo_price, "      ", cmp_6mo_gp)
    print('12 Month', "          ", cmp_12mo_price, "      ", cmp_12mo_gp)
    print('18 Month', "          ", cmp_18mo_price, "      ", cmp_18mo_gp)
        
    print(end="\n\n")
        
    # Filtering and appending
    if((cmp_6mo_gp>=0.5 and cmp_12mo_gp>=0.5 and cmp_18mo_gp>=0.5)):   # Filter crieterial 6months, 12montths, 18months - growth rate should be greater than 50 %
        good_cmp_ids.append(cmp_id)
        
        #break
        