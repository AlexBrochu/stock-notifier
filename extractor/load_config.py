import json

def load_stocks():
    # Read from config from file. 
    with open('input/stock.json') as f:
        data = json.load(f)
    
    return data

def load_portfolio():
    # Read from config from file. 
    with open('output/data.json') as f:
        portfolio = json.load(f)
    
    return portfolio

