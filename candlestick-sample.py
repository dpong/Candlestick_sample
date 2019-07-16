#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:58:55 2019

@author: dpong
"""

import pickle
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

picke_in = open('GOOGL_data_from_quandl.pickle','rb')
df = pickle.load(picke_in)





df_ohlc = df['Adj. Close'].resample('10D').ohlc()
df_vol = df['Adj. Volume'].resample('10D').sum()



df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

df_ohlc['20_ma'] = df_ohlc['close'].rolling(window=20).mean()


ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1, sharex=ax1)

ax1.xaxis_date()
ax1.plot(df_ohlc['Date'],df_ohlc['20_ma'])

candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g',colordown='r')
ax2.fill_between(df_vol.index.map(mdates.date2num),df_vol.values,0)


