class Orderbook:
    def __init__(self,user):
        self.name = ("%s's orderbook" % user.name)
        self.transactions = []
        print(("%s's Orderbook initialized" %user.name))