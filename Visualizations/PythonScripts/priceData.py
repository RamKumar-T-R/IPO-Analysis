# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:30:37 2024

@author: Ramkumar
"""

# Importing the periodical historical data

import pandas as pd
import yfinance as yf

cmp_id = 'PRINCEPIPE.NS'

tickers = yf.Ticker(cmp_id)
cmp_price_data = yf.Ticker(cmp_id).history(period="max", interval="1mo")

    

cmp_price_data = cmp_price_data.reset_index()