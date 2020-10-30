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
    try:
        print(exchange.stock_price(stock))
    except:
        "no price available"

if __name__ == "__main__":
    main()
