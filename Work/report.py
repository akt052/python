# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint

def read_portfolio(fileName):
    portfolio = []
    with open(fileName, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            d = {
                'name': row[0], 
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(d)
    return portfolio

def read_prices(fileName):
    prices = {}
    with open(fileName, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try: 
                prices[row[0]] = float(row[1])
            except:
                None
    return prices



if(len(sys.argv) == 2):
    fileName = sys.argv[1]
else:
    fileName = 'Data/portfolio.csv'

temp = read_prices(fileName)
pprint(temp)