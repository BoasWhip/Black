# -*- coding: utf-8 -*-

displayFull = False

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
    print('\n+ - + - +')
    maxSharpe = 0.0
    metrics = []
    for e in schemes:
        s = simulate(dateRange[dateFlag][0], dateRange[dateFlag][1], symbolSet, e)
        if displayFull: 
            print(s[0]),
            print(e)
        if s[0] > maxSharpe:
            maxSharpe = s[0]
            metrics = [s, e]
    print("\nPortfolio:")
    print(tuple(symbolSet))
    print("\nOptimal Weights:")
    print(metrics[1])
    print("\nPerformance Metrics:")
    print(tuple(metrics[0]))
    print('\n+ - + - +')
