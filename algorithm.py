import urllib2
import Queue
import threading
from stock import *
from yahoo_finance import Share

stock_database = []

def get_stocks(start_at, end_at, queue):
    temp_database = []
    with open('symbols.txt') as file:
        for x in range(start_at):
            file.readline()
        for x in range(end_at - start_at):
            stock = Share(file.readline().split('|')[0])
            if any(y.name == file.readline().split('|')[0] for y in temp_database):
                temp_database[y].price_list.append(stock.get_price())
            else:
                temp_database.append(Stock(file.readline().split('|')[0]))
                temp_database[len(temp_database) - 1].append_price(stock.get_price())

    queue.put(temp_database)

def update_database(database_a, database_b):
    for stock in database_b:
        database_a.append(stock)

def update_stock_list():
    url = urllib2.urlopen('ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    data = url.read()

    file = open('symbols.txt', 'w')
    file.write(data)
    file.close()

queue = [Queue.Queue(), Queue.Queue()]
threading.Thread(target = get_stocks, args = (0, 5, queue[0])).start()
threading.Thread(target = get_stocks, args = (5, 12, queue[1])).start()
update_database(stock_database, queue[0].get())
update_database(stock_database, queue[1].get())
