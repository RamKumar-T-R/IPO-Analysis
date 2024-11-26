# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:44:49 2023

@author: Ramkumar
"""

# Importing the libraries
import requests
import pandas as pd

# Creating the headers
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cookie':'defaultLang=en; nsit=yyZiRAAi0DaZN1Jd2wxPRq8t; AKA_A2=A; bm_mi=04C805BC68240E93FBBF93C932660D95~YAAQlK1NaNIHk1mMAQAAu+O5fRaqim3BWiSEVh4tMc0dCFMxHw5ugINmB63jSW3QWaKhU1UZLjZr+ft59BLE5SKTqNV6BIPHcE7sv7sgDyx9dZEcyR/DCpB5gvpGaPGk4vfW3GM6j5kAdnZPMgH+Nz0kO3ErmiSTV2XJKLvWSE7EfqO3mNB6dKnJ+XQZuoEubynPurzl9usPeUMkpW16ZeoKr5pKmrLcmhqHygDHsEvHWj9jq102k5v7fEibYM4bj7jkD+9VhmYMYyHKwUWbOZwKJ3/myC37jQ341Fo8OwHy0uGwevIF2pZ0mYN/DavbABtMGk/m~1; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwMjkxNjM5OCwiZXhwIjoxNzAyOTIzNTk4fQ.y94xOJTHTDZQuCyJeDXutje9iuPz-hitd4NG20TjI7s; nseQuoteSymbols=[{"symbol":"TATATECH","identifier":null,"type":"equity"},{"symbol":"INFY","identifier":null,"type":"equity"},{"symbol":"AWL","identifier":null,"type":"equity"},{"symbol":"TMB","identifier":null,"type":"equity"}]; ak_bmsc=EC912D792144B77001892522B17AC236~000000000000000000000000000000~YAAQlK1NaNMJk1mMAQAAZze6fRbDHdhX/pDUM8xklinlAooQQrYURZ2l/3z6LbpjtOrDhH1kUY7MOptd9k/8hWdm/XTPuMj1BZ2j+JHBXioQsJY/Wy0pnLnzPDHzBd9HrdCDcSZPPJHqVvFPxJPjWp2JgZCVUL0Qm7Sgbt/HDXhqbMwibEGyuphIVN04YHvqST87f4rj1kW8VxwDm8h2LfDtOZMwClfUF5EJFoahAGv3Cxw3gKBKeNAEdlkMiX+s+L60YoSnY+hljBDMyn8ZfAvc14LJTB9HjUKOMUy9yLjSqKQoJIi6lFSatXq4cH02+GI2bT8CsXxHcmTYO2C7E9TyB3MX1b2f/YMpu+dkt6psEeldqEVWMIkjepf2pAJOGiqpKg3KJTaSZKQjtpU98X9xC3Z9p/UQu7GVrw==; bm_sv=EA2773A2C055E1BAF8D6C93B82C55ACA~YAAQlK1NaHAKk1mMAQAA61W6fRYiAtOjY4uNwLrgROZDe2eQtBKqANucBcB4I990Z9UyyaP1kXxb7uyaRcw9iQaUu23MyHXWDo2WTxiR6vwcuwkqKY26LfLDP8o3WCMyUvguX4lyD37EN5qx+XUA420/jzum9d+VGBGnzaeNjh5SWbmp8sHGwML1CFZrS/Nm7tjP7LHu5hC9OMO45UP5ymGbawj/1jcmQRJoImf8Vj5dYSqqnbTQhZoQmoy0p4RySQ+T~1',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

# Making a request to NSEINDIA.COM
response = requests.get(url='https://www.nseindia.com/api/historical/cm/equity?symbol=AWL&series=["EQ"]&from=10-03-2023&to=12-03-2023&csv=true', headers = headers)

data = response.text

print(data)



# Note: 
    # Take care of the cookie, to cross-over the firewall of nseindia