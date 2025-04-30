# pcost.py
#
# Exercise 1.27
import csv
import sys

def calculateCost(fileName):
    cost = 0
    with open(fileName, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            numberOfShares = int(row[1])
            priceOfShares = float(row[2])
            cost += numberOfShares * priceOfShares
    return cost
def calculateCost(fileName):
    cost = 0
    with open(fileName, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        d = ["name", "shares", "price"]
        for row in rows:
            detials = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2])
            }
            cost += detials["shares"] * detials["price"]
    return cost

def calculate_cost(fileName):
    total_cost = 0
    with open(fileName, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row:{row}')
    return total_cost
            


if len(sys.argv) == 2:
    fileName = sys.argv[1]
else:
    fileName = 'Data/portfolio.csv'

cost = calculate_cost(fileName)
print(cost)




# prices = {}
# with open('Data/prices.csv', 'rt') as file:
#     for line in file:
#         row = line.split(',')
#         prices[row[0]] = float(row[1])
# print(prices)