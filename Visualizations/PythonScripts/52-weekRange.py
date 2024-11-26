# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:44:01 2024

@author: Ramkumar
"""

import yfinance as yf
import pandas as pd

cmp_id = 'PRINCEPIPE.NS'
info = yf.Ticker(cmp_id).info

infoDF = pd.DataFrame(info)
infoDF.drop(infoDF.tail(9).index,inplace=True)
infoDF = infoDF.transpose()
infoDF = infoDF.reset_index()


# For getting the data for 52-week range:
    
#52week_low = CALCULATE( SUM(infoDF[Details]), FILTER(infoDF, [Index] = "fiftyTwoWeekLow"))