#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.environ['IEX_TOKEN'] = "sk_a9ccbee140454466bf7da631df08acc0"
from datetime import datetime
import dateparser
import re


from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
import matplotlib.pyplot as plt


def give_stockprice(stock) -> str:
    """Get stockPrice form IEX
    """
    stock = Stock(stock)
    price = stock.get_price().to_string()
    price_string = re.search(r'((\d*\.)?\d+)', price).group(1)
    print(price_string)
    return price_string

def get_historical_figure(stock,start_time, end_time) -> None:
    start = dateparser.parse(start_time)
    end = dateparser.parse(end_time)
    df = get_historical_data("AAPL", start, end)
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df['open'])
    figure_name = stock + '.png'
    plt.savefig('stock.name')
