from user import User
from portfolio import Portfolio
from exchange_bram import Exchange

def main():
    print("Investment Game")
    user = User()
    portfolio = Portfolio(user)
    print (user)
    print (portfolio)
    print (exchange)
    print (exchange.available_stocks())

if __name__ == "__main__":
    main()
