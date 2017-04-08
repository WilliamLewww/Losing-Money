import Queue
import threading
import time
import urllib2
import cPickle as pickle
from stock import *

stock_database = []

def get_stocks(start_at, end_at):
    temp_database = []
    with open('symbols.txt') as file:
        for x in range(start_at):
            file.readline()
        for x in range(end_at - start_at):
            line = file.readline()
            temp_database.append(Stock(line.split('|')[0]))

    return temp_database

def update_database(database_a, database_b):
    for stock in database_b:
        database_a.append(stock)

def update_stock_list():
    url = urllib2.urlopen('ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    data = url.read()

    file = open('symbols.txt', 'w')
    file.write(data)
    file.close()

def append_prices(database):
    queue_list = [Queue.Queue() for x in range(len(database))]
    for x in range(len(database)):
        threading.Thread(target = get_price, args = (database[x].name, queue_list[x],)).start()

    for x in range(len(database)):
        database[x].append_price(queue_list[x].get())

def remove_null(database):
    queue_list = [Queue.Queue() for x in range(len(database))]
    for x in range(len(database)):
        threading.Thread(target = get_price, args = (database[x].name, queue_list[x],)).start()

    return [database[x] for x in range(len(database)) if queue_list[x].get() != None]

def save_database(database):
    with open('database.pkl', 'wb') as file:
        pickle.dump(database, file, -1)

def load_database():
    with open('database.pkl', 'rb') as file:

        return pickle.load(file)

try:
    stock_database = load_database()
    if len(stock_database) == 0:
        update_database(stock_database, get_stocks(0, 3))
        stock_database = remove_null(stock_database)
    while True:
        if threading.active_count() == 1:
            append_prices(stock_database)

        time.sleep(1)
except KeyboardInterrupt:
    save_database(stock_database)
    pass
