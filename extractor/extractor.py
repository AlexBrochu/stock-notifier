import yfinance as yf
import json

def write_info_to_file(data):

    converted = json.dumps(data, indent=4, sort_keys=True)
    with open('output/data.json', 'w') as outfile:
        outfile.write(str(converted))


def load_info_from_file():
    with open('output/data.json') as f: 
        data = f.read() 
    
    print("Data type before reconstruction : ", type(data)) 
        
    # reconstructing the data as a dictionary 
    js = json.loads(data) 
    
    print("Data type after reconstruction : ", type(js)) 
    print(js) 

def extract_portfolio_stats(portfolio):
    portfolio_stats = {
        "total_value": 0
    }
    for sector in portfolio:
        
        portfolio[sector]['total_value'] = 0
        for stock in portfolio[sector]['stocks']:
            portfolio[sector]['total_value'] += stock['current_price']*stock['quantity']

        portfolio_stats['total_value'] += portfolio[sector]['total_value']

    # calcule percentage
    for sector in portfolio:
        portfolio[sector]['percentage'] = portfolio[sector]['total_value']/portfolio_stats['total_value']

    portfolio_stats['details'] = portfolio  
    return portfolio_stats

def build_portfolio(data):
    portfolio = {}
    for stock in data['stocks']:
        tick = yf.Ticker(stock['name'])
        data = tick.history()
        last_quote = (data.tail(1)['Close'].iloc[0])
        stock['current_price'] = last_quote

        current_sector = tick.info['sector']

        if not current_sector in portfolio:
            portfolio[current_sector] = {
                "total_value": 0,
                "percentage": 0,
                "stocks" : list()
            }
            portfolio[current_sector]['stocks'].append(stock)
        else:
            portfolio[current_sector]['stocks'].append(stock)
    return portfolio
