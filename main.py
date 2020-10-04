from extractor.load_config import load_stocks as ld
import extractor.extractor as e
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pandas_datareader import data as pdr

import yfinance as yf

data = ld()

portfolio = e.build_portfolio(data)
# extract portfolio stats 
portfolio_stats = e.extract_portfolio_stats(portfolio)

e.write_info_to_file(portfolio_stats)
e.load_info_from_file()
