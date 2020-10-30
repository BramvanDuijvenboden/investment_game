#!/usr/bin/env python

from exchange import Exchange
from portfolio import Portfolio
from user import User


def main():
    name = "Bram"
    print("Investment Game")
    user = User(name)
    portfolio = Portfolio(user)
    exchange = Exchange()
    user.buy(exchange,portfolio)
    portfolio.overview()


if __name__ == "__main__":
    main()


