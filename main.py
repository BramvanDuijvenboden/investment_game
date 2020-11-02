#!/usr/bin/env python

from exchange import Exchange
from portfolio import Portfolio
from user import User
from orderbook import Orderbook
import sys


def main():
    name = input("Enter your username")
    print("Investment Game")
    user = User(name)
    portfolio = Portfolio(user)
    orderbook=Orderbook(user)
    exchange = Exchange()
    while True:
        action = int(input("What do you want to do? Press 1 to buy, 2 to sell, 3 to quit, 4 to show orderbook, 5 to show portfolio:"))
        if action == 1:
            user.buy(exchange,portfolio,orderbook)
        elif action == 2:
            user.sell(exchange, portfolio, orderbook)
        elif action == 3:
            orderbook.orders()
        elif action == 4:
            portfolio.overview()
        elif action == 5:
            sys.exit()

        else:
            print("Choose something else")

if __name__ == "__main__":
    main()


