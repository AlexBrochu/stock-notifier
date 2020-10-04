import notify2
import yfinance as yf

def notify_stock(stock_name, stock_price, stock_limit_buy):
    notify2.init("Stock Notifier")
    n = notify2.Notification(None, icon='notification-display-brightness-full')

    # set urgency level 
    n.set_urgency(notify2.URGENCY_NORMAL) 
    
    # set timeout for a notification 
    n.set_timeout(10000) 

    n.update("Time to buy: Stock " + stock_name, "Current price is " + str(stock_price) + " your limit buy price is " + str(stock_limit_buy))
    n.show()
    
def get_current_stock_price(stock, limit_buy):
    tick = yf.Ticker(stock)
    data = tick.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print("" + str(last_quote) + " ---- " + str(limit_buy))
    if last_quote <= limit_buy:
        print("limit buy hit")
        notify_stock(stock, last_quote, limit_buy)


def notify_when_stock(portfolio):

    details = portfolio['details']
    for sector in details:
        stocks = details[sector]['stocks']
        for stock in stocks:
            print("start stock thread " + stock['name'])
            get_current_stock_price(stock['name'], stock['limit-buy'])
