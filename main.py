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
        action = input("What do you want to do? (buy, sell, quit, show orderbook, show portfolio):")
        if action == 'buy':
            user.buy(exchange,portfolio,orderbook)
        elif action == 'sell':
            user.sell(exchange, portfolio, orderbook)
        elif action == "show orderbook":
            orderbook.orders()
        elif action == "show portfolio":
            portfolio.overview()
        elif action == 'quit':
            sys.exit()

        else:
            print("Choose something else")

if __name__ == "__main__":
    main()


