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

def update_portfolio_stats(portfolio_stats):
    portfolio_stats['total_value'] = 0
    portfolio_details = portfolio_stats['details']

    for sector in portfolio_details:
        portfolio_details[sector]['total_value'] = 0
        for stock in portfolio_details[sector]['stocks']:
            portfolio_details[sector]['total_value'] += stock['current_price']*stock['quantity']

        portfolio_stats['total_value'] += portfolio_details[sector]['total_value']

        # calcule percentage
        portfolio_details[sector]['percentage'] = portfolio_details[sector]['total_value']/portfolio_stats['total_value']
    
    return portfolio_stats

def extract_portfolio_stats(portfolio):
    portfolio_stats = {
        "total_value": 0
    }
    portfolio_stats['details'] = portfolio 
    
    portfolio_stats = update_portfolio_stats(portfolio_stats) 

    # for sector in portfolio:
        
    #     portfolio[sector]['total_value'] = 0
    #     for stock in portfolio[sector]['stocks']:
    #         portfolio[sector]['total_value'] += stock['current_price']*stock['quantity']

    #     portfolio_stats['total_value'] += portfolio[sector]['total_value']

    # # calcule percentage
    # for sector in portfolio:
    #     portfolio[sector]['percentage'] = portfolio[sector]['total_value']/portfolio_stats['total_value']

    
    return portfolio_stats

def build_portfolio(data):
    portfolio = {}
    for stock in data['stocks']:
        print("extract " + stock['name'])
        tick = yf.Ticker(stock['name'])
        data = tick.history()
        last_quote = (data.tail(1)['Close'].iloc[0])
        stock['current_price'] = last_quote
        stock['total_price'] = stock['current_price'] * stock['quantity']

        if 'sector' in tick.info.keys(): 
            current_sector = tick.info['sector']
        else:
            current_sector = 'index'

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
