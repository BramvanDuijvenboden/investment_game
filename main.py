from user import User
from portfolio import Portfolio

def main():
    print("Investment Game")
    user = User()
    portfolio = Portfolio(user)
    print (user)
    print (portfolio)

if __name__ == "__main__":
    main()
