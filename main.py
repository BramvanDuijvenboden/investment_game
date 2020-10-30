#!/usr/bin/env python

from exchange_bram import Exchange
from portfolio import Portfolio
from user import User


def main():
    print("Investment Game")
    user = User()
    portfolio = Portfolio(user)
    print (user)
    print (portfolio)
    exchange = Exchange()
    print (exchange)
    stock = exchange.available_stocks()
    print(exchange.stock_price(stock))


if __name__ == "__main__":
    main()
