from yahoo_finance import Share

def get_price(name, queue):
    error = 0
    while error == 0:
        try:
            queue.put(Share(name).get_price())
            error = 1
        except:
            pass

class Stock:
    def __init__(self, name):
        self.name = name
        self.price_list = []

    def append_price(self, price):
        self.price_list.append(price)
