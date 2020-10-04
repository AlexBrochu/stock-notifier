import json

def load_stocks():
    # Read from config from file. 
    with open('input/stock.json') as f:
        data = json.load(f)
    
    return data
