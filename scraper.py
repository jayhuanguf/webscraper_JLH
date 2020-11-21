import json
import csv
import re
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1447977600&period2=1605744000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

response = requests.get(url_stats)

soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
date_soup = soup.find_all('td', {'class': 'Py(10px) Ta(start) Pend(10px)'})

length = len(date_soup)
print(length)
for i in range(0, length):
    print(date_soup[i].text)

