import notify2
import yfinance as yf

def notify_stock(stock_name, stock_price, stock_limit_buy):
    notify2.init("Stock Notifier")
    n = notify2.Notification(None, icon='notification-display-brightness-full')

    # set urgency level 
    n.set_urgency(notify2.URGENCY_NORMAL) 
    
    # set timeout for a notification 
    n.set_timeout(10000) 

    n.update("Time to buy: Stock " + stock_name, "Current price is " + str(stock_price) + "$ your limit buy price is " + str(stock_limit_buy) + "$")
    n.show()
    
def get_current_stock_price(stock):
    tick = yf.Ticker(stock['name'])
    data = tick.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print("" + str(last_quote) + " ---- " + str(stock['limit-buy'])
    if last_quote <= stock['limit-buy']:
        print("limit buy hit")
        notify_stock(stock['name'], last_quote, stock['limit-buy'])

    
    stock['total-price'] = last_quote * stock['quantity']
    return stock


def notify_when_stock(portfolio):

    details = portfolio['details']
    for sector in details:
        stocks = details[sector]['stocks']
        for stock in stocks:
            print("start stock thread " + stock['name'])
            stock = get_current_stock_price(stock)

    return portfolio
