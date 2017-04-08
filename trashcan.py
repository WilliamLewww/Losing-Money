def save_database(database):
    file = open('database.txt', 'w')
    for stock in database:
        file.write(str(stock.name) + "|" + "/".join(str(x) for x in stock.price_list) + "\n")
    file.close()
    pass

def load_database(database):
    with open('database.txt') as file:
        for line in file:
            database.append(Stock(line.split('|')[0], [x for x in line.split('|')[1].replace("\n", "").split('/')]))
