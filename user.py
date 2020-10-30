#Hereby we want to have a buy a and sell interaction which needs to interact between the exchange and portfolio
# The User needs to have a budget and remaining balance (Budget - invested money)

class User:
    def __init__(self, name):
        self.name = name
        self.balance= 100000
        print("Username is " + self.name + ". " + "Your balance is $" + str(self.balance))

    def buy(self, exchange,portfolio):
        print("You have chosen to buy stocks")
        stock = exchange.available_stocks()
        price = exchange.stock_price(stock)
        buy = input(("Would you like to buy", stock, "at", price, "per share? (Y/N)"))
        if buy=="Y":
            try:
                quantity = int(input("How many share would you like to buy?"))
            except:
                print("That is not a whole number")
            if price*quantity >= self.balance:
                print("Insuficient funds")
            else:
                print("you have bought", quantity, stock, "shares, at a price of", price, ", at a total amount of", price*quantity)
                self.balance -= price*quantity
                if stock in portfolio.holdings:
                    portfolio.holdings[stock] += quantity
                else:
                    portfolio.holdings[stock] = quantity
                print("Stock added to portfolio. Your current balance is $", str(self.balance))


        else:
            print("You are not buying")

