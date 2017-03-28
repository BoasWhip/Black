
# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
startDate = dt.datetime(2006, 1, 1)
endDate = dt.datetime(2010, 12, 31)
nameFile = 'W1Run'
rootDir = '/Users/oozsan/Desktop/Black/Project Black/Data/W1'

def dataImport(startDate, endDate, symbolsList):
    dt_timeofday = dt.timedelta(hours=16)
    dt_start = startDate
    dt_end = endDate
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)
    na_price = d_data['close'].values

def dataExport(dataFile, nameFile):
    rootDir = '/Users/oozsan/Desktop/Black/Project Black/Data/W1'

def dataPlot(dataFile, nameFile):
    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.plot(ldt_timestamps, na_price)
    plt.legend(ls_symbols)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.savefig('adjustedclose.pdf', format='pdf')

    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]

    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.plot(ldt_timestamps, na_normalized_price)
    plt.legend(ls_symbols)
    plt.ylabel('Normalized Close')
    plt.xlabel('Date')
    plt.savefig('normalized.pdf', format='pdf')

    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()

    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)

    # Plotting the plot of daily returns
    plt.clf()
    plt.plot(ldt_timestamps[0:50], na_rets[0:50, 3])  # $SPX 50 days
    plt.plot(ldt_timestamps[0:50], na_rets[0:50, 4])  # XOM 50 days
    plt.axhline(y=0, color='r')
    plt.legend(['$SPX', 'XOM'])
    plt.ylabel('Daily Returns')
    plt.xlabel('Date')
    plt.savefig('rets.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between XOM VS $SPX
    plt.clf()
    plt.scatter(na_rets[:, 3], na_rets[:, 4], c='blue')
    plt.ylabel('XOM')
    plt.xlabel('$SPX')
    plt.savefig('scatterSPXvXOM.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between $SPX VS GLD
    plt.clf()
    plt.scatter(na_rets[:, 3], na_rets[:, 1], c='blue')  # $SPX v GLD
    plt.ylabel('GLD')
    plt.xlabel('$SPX')
    plt.savefig('scatterSPXvGLD.pdf', format='pdf')

def main():
    closeData = dataImport(startDate, endDate, symbols)
    print closeData

if __name__ == '__main__':
    main()

print(symbols)
