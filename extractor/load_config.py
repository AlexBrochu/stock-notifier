import json

def load_stocks():
    # Read from config from file. 
    with open('stock.json') as f:
        data = json.load(f)
    
    return data
