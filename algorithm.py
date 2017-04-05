import urllib2
from stock import *
from yahoo_finance import Share

stock_database = []

def update_database():
    with open('symbols.txt') as file:
        for x in range(5):
            stock = Share(file.readline().split('|')[0])
            if any(x.name == file.readline().split('|')[0] for x in stock_database):
                stock_database[x].price_list.append(stock.get_price())
            else:
                stock_database.append(Stock(file.readline().split('|')[0]))
                stock_database[len(stock_database) - 1].append_price(stock.get_price())

def update_stock_list():
    url = urllib2.urlopen('ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    data = url.read()

    file = open('symbols.txt', 'w')
    file.write(data)
    file.close()

update_stock_list()
update_database()
print(len(stock_database))
