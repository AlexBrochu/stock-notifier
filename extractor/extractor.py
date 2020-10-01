from load_config import load_stocks as ls
import yfinance as yf
import json

def write_info_to_file(data):

    converted = json.dumps(data)
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
stock = "BPY-UN.TO"
tick = yf.Ticker(stock)
# get stock info
#print(tick.info)

currentSector = tick.info['sector']
print(currentSector)

if not currentSector in contentFile:
    contentFile = {
        currentSector: set()
    }
    contentFile[currentSector].add(stock)
    print("add content")
else:
    contentFile[currentSector].add("BPY")

# convert set to list
contentFile['Real Estate'] = list(contentFile['Real Estate'])

print(contentFile)
write_info_to_file(contentFile)
load_info_from_file()

#for stock in data:

