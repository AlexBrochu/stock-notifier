import notify2
import yfinance as yf
import extractor.extractor as e
from currency_converter import CurrencyConverter

c = CurrencyConverter()

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
    name = stock['name']
    buy_price = stock['limit-buy']

    tick = yf.Ticker(name)
    data = tick.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print("" + str(last_quote) + " ---- " + str(buy_price))

    if last_quote <= buy_price:
        print("limit buy hit")
        notify_stock(name, last_quote, buy_price)

    if 'currency' in stock.keys():
        currency = stock['currency']
        last_quote = c.convert(last_quote, currency.upper(), 'CAD')
    # update last quote in CAD
    stock['current_price'] = last_quote

    stock['total_price'] = last_quote * stock['quantity']
    return stock

def notify_when_stock(portfolio):

    details = portfolio['details']
    for sector in details:
        stocks = details[sector]['stocks']
        for stock in stocks:
            print("start stock thread " + stock['name'])
            stock = get_current_stock_price(stock)

    return e.update_portfolio_stats(portfolio)
