class Orderbook:
    def __init__(self,user):
        self.name = ("%s's orderbook" %user.name)
        self.transactions = []
        print(("%s initialized" %user.name))

    def orders(self):
        for transaction in self.transactions:
            print(transaction)