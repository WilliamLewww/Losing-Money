class Stock:
    def __init__(self, name):
        self.name = name
        self.price_list = []

    def append_price(self, price):
        self.price_list.append(price)
