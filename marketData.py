# -*- coding: utf-8 -*-

import numpy as np
from pandas import read_csv as importDB
import pandas as pd

database = r'\\UBSPROD.MSAD.UBS.NET\UserData\ozsanos\RF\Desktop\Black\stockData.csv'
tickers = ['AAPL','ADBE','ADI','AMD','AXP','BRCM','C','GLD','GOOG','GS','HNZ','HPQ','IBM','MSFT','TXN','XOM']
dateRange = [("2010-01-01","2010-12-31"),("2011-01-01","2011-12-31")]
# dateRange = pd.date_range(startDate, endDate)

'''
    Pre-weightings permutations
'''
schemes = []
points = range(0, 11, 1)
for i in points:
    for j in points:
        for k in points:
            z = i + j + k
            if z <= 10:
                schemes.append((round(i/10.0,1), round(j/10.0,1), round(k/10.0,1), round(1.0 - z/10.0,1)))
schemes = tuple(schemes)

'''
    *** Code Body ***
'''

def getData(startDate, endDate, symbolSet):
    return importDB(database, usecols = ['Close'] + symbolSet, index_col = 'Close').loc[startDate : endDate]
    
def simulate(startDate, endDate, symbolSet, weights):
    marketData = getData(startDate, endDate, symbolSet).values
    days = len(marketData)
    portfolio = np.zeros(days)
    returns = portfolio.copy()
    for e in range(len(marketData[0])):
        marketData[:,e] = weights[e] * marketData[:,e] / marketData[0,e]
        portfolio += marketData[:,e]
    for e in range(days):
        if e > 0: returns[e] = (portfolio[e]/portfolio[e-1]) - 1
    meanDailyReturn = np.average(returns)
    stdDailyReturn = np.std(returns)
    cummDailyReturn = portfolio[-1]
    SharpeRatio = (days**0.5) * (meanDailyReturn / stdDailyReturn)
    return [round(SharpeRatio,6), round(meanDailyReturn,6), round(stdDailyReturn,6), round(cummDailyReturn,6)]

def optimise(symbolSet, dateFlag):
    maxSharpe = 0.0
    metrics = []
    for e in schemes:
        #print e,
        s = simulate(dateRange[dateFlag][0], dateRange[dateFlag][1], symbolSet, e)
        #print s
        if s[0] > maxSharpe:
            maxSharpe = s[0]
            metrics = [s, e]
    print('\n+ - + - +')
    print "\nPortfolio:"
    print tuple(symbolSet)
    print "\nOptimal Weights:"
    print metrics[1]
    print "\nPerformance Metrics:"
    print tuple(metrics[0])
    print('\n+ - + - +\n\n\n\n')

'''
    Portfolios
'''
'''
# Test 1
optimise(['AAPL', 'GLD', 'GOOG', 'XOM'], True)
# Test 2
optimise(['AXP', 'HPQ', 'IBM', 'HNZ'], False)
'''
# Quiz 1
optimise(['AAPL', 'GOOG', 'IBM', 'MSFT'], True)
# Quiz 2
optimise(['BRCM', 'ADBE', 'AMD', 'ADI'], False)
# Quiz 3
optimise(['BRCM', 'TXN', 'AMD', 'ADI'], True)
# Quiz 4
optimise(['BRCM', 'TXN', 'IBM', 'HNZ'], False)
# Quiz 5
optimise(['C', 'GS', 'IBM', 'HNZ'], False)

'''
# Test 1
is2011 = True
symbolSet = ['AAPL', 'GLD', 'GOOG', 'XOM']
weights = [0.4,0.4,0.0,0.2]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')

# Test 2
is2011 = False
symbolSet = ['AXP', 'HPQ', 'IBM', 'HNZ']
weights = [0.0,0.0,0.0,1.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')
'''

# Quiz 1
is2011 = True
symbolSet = ['AAPL', 'GOOG', 'IBM', 'MSFT']
weights = [0.5,0.0,0.5,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.2,0.0,0.8,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.2,0.2,0.2,0.4]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.1,0.1,0.8,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')

# Quiz 2
is2011 = False
symbolSet = ['BRCM', 'ADBE', 'AMD', 'ADI']
weights = [0.0,0.2,0.8,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.0,0.0,0.0,1.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [1.0,0.0,0.0,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.0,0.0,0.1,0.9]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')

# Quiz 3
is2011 = True
symbolSet = ['BRCM', 'TXN', 'AMD', 'ADI']
weights = [0.0,0.0,0.8,0.2]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.0,0.2,0.0,0.8]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.0,0.0,0.1,0.9]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.0,0.0,0.0,1.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')

# Quiz 4
is2011 = False
symbolSet = ['BRCM', 'TXN', 'IBM', 'HNZ']
weights = [0.1,0.1,0.6,0.2]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.3,0.0,0.7,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.1,0.1,0.0,0.8]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.4,0.4,0.0,0.2]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')

# Quiz 5
is2011 = False
symbolSet = ['C', 'GS', 'IBM', 'HNZ']
weights = [0.0,0.0,1.0,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.2,0.0,0.0,0.8]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.4,0.6,0.0,0.0]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
weights = [0.2,0.2,0.4,0.2]
print simulate(dateRange[is2011][0], dateRange[is2011][1], symbolSet, weights)
print('\n')