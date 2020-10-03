from load_config import load_stocks as ls
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


data = ls()

contentFile = {}
for stock in data['stocks']:
    tick = yf.Ticker(stock['name'])
    data = tick.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    stock['current_price'] = last_quote

    currentSector = tick.info['sector']

    if not currentSector in contentFile:
        contentFile[currentSector] = {
            "total_value": 0,
            "percentage": 0,
            "stocks" : list()
        }
        contentFile[currentSector]['stocks'].append(stock)
    else:
        contentFile[currentSector]['stocks'].append(stock)

# extract portfolio stats
portfolio_stats = {
    "total_value": 0
}
for sector in contentFile:
    
    contentFile[sector]['total_value'] = 0
    for stock in contentFile[sector]['stocks']:
        contentFile[sector]['total_value'] += stock['current_price']*stock['quantity']

    portfolio_stats['total_value'] += contentFile[sector]['total_value']

# calcule percentage
for sector in contentFile:
    contentFile[sector]['percentage'] = contentFile[sector]['total_value']/portfolio_stats['total_value']

portfolio_stats['details'] = contentFile   

print(portfolio_stats)
write_info_to_file(portfolio_stats)
load_info_from_file()

#for stock in data:

