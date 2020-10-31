# We want to start by defining a class/portfolio
# Dictionary that keeps track of how much stock the User has bought and which one of the exchange
# In order to have a return of the investment we need to be able to have the price of the stock and the price for which the stock was bought, Return = Price of stock - price paid

class Portfolio:
    def __init__(self,user):
        self.name = ("%s's portfolio" % user.name)
        self.holdings = {}
        print(self.name)

    def overview(self):
        for holding in self.holdings:
            print("You hold", self.holdings[holding], "shares in", holding)


