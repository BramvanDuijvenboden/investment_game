import pandas as pd

class User:
    def __init__(self, name):
        self.name = name
        self.balance= 100000
        print("Username is " + self.name + ". " + "Your balance is $" + str(self.balance))

    def buy(self, exchange,portfolio,orderbook):
        print("You have chosen to buy stocks")
        stock = exchange.available_stocks()
        price_info = exchange.stock_price(stock)
        price = price_info['low']
        buy = input(("Would you like to buy", stock, "at", price, "per share? (Y/N)")).upper()
        if buy=="Y":
            try:
                quantity = int(input("How many shares would you like to buy?"))
            except:
                print("That is not a whole number")
            if price*quantity > self.balance:
                print("Insuficient funds")
            else:
                self.balance -= price*quantity
                if stock in portfolio.holdings:
                    portfolio.holdings[stock]['quantity'] += quantity
                    portfolio.holdings[stock]['costprice'] += price*quantity
                else:

                    portfolio.holdings[stock]= {'quantity': quantity, 'costprice':price * quantity}
                orderbook.transactions.append({'timestamp':pd.Timestamp.now(),'stock':stock,'price':price,
                                               'price timestamp':price_info.name,'quantity':quantity,'buy/sell':"Buy"})
                print("you have bought", quantity, stock, "shares, at a price of", price, ", with a total amount of",
                      price * quantity, ". The stock is added to your portfolio. Your current balance is $",
                      str(self.balance))
        else:
            print("You are not buying")

    def sell(self,exchange,portfolio,orderbook):
        print("You have chosen to sell stocks")
        stock = exchange.available_stocks()
        price_info = exchange.stock_price(stock)
        price = price_info['high']
        sell = input(("Would you like to sell", stock, "at", price, "per share? (Y/N)")).upper()
        if sell == "Y":
            try:
                quantity = int(input("How many shares would you like to sell?"))
            except:
                print("That is not a whole number")
            try:
                if quantity > portfolio.holdings[stock]['quantity']:
                    print("You do not have enough shares to sell")
                else:
                    self.balance += price * quantity
                    portfolio.holdings[stock]['costprice'] -= quantity * portfolio.average_costprice(stock)
                    portfolio.holdings[stock]['quantity'] -= quantity

                    orderbook.transactions.append({'timestamp': pd.Timestamp.now(), 'stock': stock, 'price': price,
                                                   'price timestamp': price_info.name, 'quantity': quantity,
                                                   'buy/sell': "Sell"})
                    print("you have sold", quantity, stock, "shares, at a price of", price, ", with a total amount of",
                          price * quantity, ". The shares are removed from your portfolio. Your current balance is $",
                          str(self.balance))
            except:
                print(stock, "is not in your portfolio")

        else:
            print("You are not selling")
