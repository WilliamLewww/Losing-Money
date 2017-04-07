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
    def __init__(self, name, price_list = []):
        self.name = name

        if len(price_list) == 0:
            self.price_list = []
        else:
            self.price_list = price_list

    def set_name(self, name):
        self.name = name

    def simplify_repetition(self):
        pass

    def set_price_list(self, price_list):
        self.price_list = price_list

    def append_price(self, price):
        self.price_list.append(price)
