import json
import csv
import re
from io import StringIO
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import itertools

date_list, price_list= [], []

url_stats = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1448064000&period2=1605916800&interval=1wk&filter=history&frequency=1wk&includeAdjustedClose=true'

response = requests.get(url_stats)

soup = BeautifulSoup(response.text, 'lxml')

date_soup = soup.find_all('td', {'class': 'Py(10px) Ta(start) Pend(10px)'})
price_soup = soup.find_all('td', {'class': 'Py(10px) Pstart(10px)'})

for date in date_soup:
    date_list.append(date.text)
for price in price_soup:
    price_list.append(price.text)

open_price_list = [float(i.replace(',','')) for i in price_list[::6]]
# print(date_list)
plt.plot(price_list[0:10:6])
# print(open_price_list)
plt.plot_date(date_list, open_price_list)
plt.show()
