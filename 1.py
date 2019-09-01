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



def addTechnicalAnalysisIndicators(df):
	df['rsi'] = ta.rsi(close, n=14)
	df['obv'] = ta.on_balance_volume(close, volume, fillna=False)
	return df

df = addTechnicalAnalysisIndicators(df)

print(df.head())
