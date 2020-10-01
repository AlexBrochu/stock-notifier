from load_config import load_stocks as ld

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pandas_datareader import data as pdr

import yfinance as yf
msft = yf.Ticker("BPY-UN.TO")

# get stock info
print(msft.info)
#print(msft.history(period="max"))


#print(ac)

data = ld()
print(data['stocks'])
