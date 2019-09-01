import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
from datetime import datetime
from itertools import repeat
import ta

df pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&apikey=06KC1KI7VRYHJ88L&datatype=csv', sep = ',')

open = df['open']
close = df['close']
high = df['high']
low = df['low']
vol = df['volume']
uvol = df['uvol']
dvol = df['dvol']
vold = df['vold']


def addTechnicalAnalysisIndicators(df):
	df['rsi'] = ta.rsi(close, n=14)
	if  
	return df

def addVol(df)
	current_stock_price = close.iloc[i]
	prev_stock_price = close.iloc[i-1]
	if current_stock_price > prev_stock_price
		df['UVOL'] += vol
	if current_stock_price < prev_stock_price
		df['DVOL'] += vol
	return df
	
def addVold(df)
	df['vold'] = uvol/dvol
	return df

df = addTechnicalAnalysisIndicators(df)
df = addVol(df)
df = addVold(df)

print(df.head())
