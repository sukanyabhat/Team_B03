# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:46:37 2016

@author: sukanyabhat
"""
import pandas as pd
#numpy for numerical manipulation
#import numpy as np
#to plot
import matplotlib.pylab as plt

#for adjusted dickey fuller test
from statsmodels.tsa.stattools import adfuller
def timeseries(ts):
    plt.plot(ts)
    #taking span of 30 since it is daily data
    rolmean = pd.rolling_mean(ts, window=30)
    rolstd = pd.rolling_std(ts, window=30)
    
    #Plot rolling statistics:
    plt.plot(ts, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(ts, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
        print (dfoutput)

