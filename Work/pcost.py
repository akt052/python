# pcost.py
#
# Exercise 1.27
cost = 0
with open('./Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        numberOfShares = int(row[1])
        priceOfShares = float(row[2])
        cost += numberOfShares * priceOfShares
print(cost)