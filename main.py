from extractor.load_config import load_stocks, load_portfolio
from notification.notifier import notify_when_stock
import extractor.extractor as e
import threading
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#from datetime import datetime
#from pandas_datareader import data as pdr

def setup_portfolio():
    data = load_stocks()

    portfolio = e.build_portfolio(data)
    # extract portfolio stats 
    portfolio_stats = e.extract_portfolio_stats(portfolio)

    e.write_info_to_file(portfolio_stats)
    e.load_info_from_file()

def thread_notify(portfolio):
    notify_when_stock(portfolio)
    threading.Timer(10, thread_notify, args=(portfolio,)).start()

## Setup porfolio
#setup_portfolio()

## Notify when stock reach asked value
portfolio = load_portfolio()

thread_notify(portfolio)
