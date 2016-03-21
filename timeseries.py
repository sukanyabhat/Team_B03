# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:45:45 2016

@author: JokerSoup
"""

import pandas as pd
#numpy for numerical manipulation
#import numpy as np
#to plot
import matplotlib.pylab as plt
from rpy2 import *
import rpy2.robjects as RO
from rpy2.robjects import globalenv

#for adjusted dickey fuller test
from statsmodels.tsa.stattools import adfuller

def timeseries(abc):
    plt.plot(abc)
    #taking span of 30 since it is daily data
    rolmean = pd.rolling_mean(abc, window=30)
    rolstd = pd.rolling_std(abc, window=30)
      
    #Plot rolling statistics:
    plt.plot(abc, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    globalenv['abc'] = abc
    RO.r('fit_arima <- auto.arima(ts(abc,frequency=7))')
#    RO.r('fit_ets <- ets(ts(abc,frequency=7))')
#    RO.r('pred<-ifelse(AIC(fit_arima)<AIC(fit_ets),forecast(fit_arima,h=1),forecast(fit_ets,h=1))')
    RO.r('pred<-forecast(fit_arima,h=1)')    
    RO.r('prediction<-pred$mean[1]')
    RO.r('prediction_min<-pred$lower[2]')
    RO.r('prediction_max<-pred$upper[2]')
    pandas2ri.activate()
    x = pandas2ri.ri2py(r['prediction'])
    y = pandas2ri.ri2py(r['prediction_min'])
    z = pandas2ri.ri2py(r['prediction_max'])
    events= []
    xyz = {'PRED':x, 'MIN':y, 'MAX':z}
    print(xyz)  
    
#    for key in abc.keys():
#        if abc[key] > rolmean[key]+3*rolstd[key]:
#            events.append(key)
#    for key in abc.keys():
#        if abc[key] < rolmean[key]-2*rolstd[key]:
#            events.append(key)
 
    return events           
    
    #Perform Dickey-Fuller test:
#    print ('Results of Dickey-Fuller Test:')
#    dftest = adfuller(ts, autolag='AIC')
#    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
#    for key,value in dftest[4].items():
#        dfoutput['Critical Value (%s)'%key] = value
#        print (dfoutput)
