
#Hereby we want to have a buy a and sell interaction which needs to interact between the exchange and portfolio
# The User needs to have a budget and remaining balance (Budget - invested money)
from exchange_bram import Exchange
class User:
    def __init__(self, name):
        self.name = name
        self.balance= 100000
        print("Username is " + self.name + ". " + "Your balance is $" + str(self.balance))

    def buy(self, exchange):
        print("You have chosen to buy stocks")
        stock = exchange.available_stocks()
        return exchange.stock_price(stock)

