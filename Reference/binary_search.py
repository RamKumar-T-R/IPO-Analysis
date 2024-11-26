# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:43:09 2024

@author: Ramkumar
"""
import yfinance as yf
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
from time import sleep

# Function for searching the increased price value of the ticker
def binary_search(cmp_id, price):
    cmp_price_data = yf.Ticker(cmp_id).history(period='max', interval='1d')
    
    if(cmp_price_data.iloc[cmp_price_data.shape[0]-1, :]['Close'] < price):
        print('The expected growth is not yet met')
        return 0
    
    
    start_date = cmp_price_data.iloc[0, :].name.date()
    end_date = cmp_price_data.iloc[cmp_price_data.shape[0]-1, :].name.date()
    
    while(True):
        mid_date = start_date + (end_date - start_date)/2
        mid_date = yf.Ticker(cmp_id).history(start=str(mid_date), end=str(mid_date + relativedelta(days=15)), interval='1d').iloc[0, :].name # Updating the date to an availabe one
        #print(start_date, "    ", end_date, "    ", mid_date)
        
        if(start_date >= (end_date - relativedelta(days=10))):
            print("The search value for",  price, ":")
            print(cmp_price_data.loc[mid_date], end='\n\n')
            return mid_date.date()
        
        
        elif(price > cmp_price_data.loc[mid_date]['Close']):
            start_date = mid_date.date()
            
        else:
            end_date = mid_date.date()