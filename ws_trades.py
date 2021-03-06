#!/usr/bin/env python

#
#The MIT License (MIT)
#
#Copyright (c) 2016 Mario Romero 
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

##parent folder import hack 
import sys
import os
from datetime import datetime
import pytz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##


#from bitso import Client, Listener
from bitso import *

utc=pytz.UTC

class BasicBitsoListener(Listener):
    def on_connect(self):
        print("Connected")
        
    def on_update(self, data):
        for obj in data.updates:
            print(obj)
        
if __name__ == '__main__':
    api = Api()
    # api = Api(key, secret, timeout)
    trades = api.trades("btc_usd", marker=None, limit=1, sort='desc')
    timezone = trades[0].created_at.tzinfo
    today = datetime.now(timezone)
    print(today)
    # today_utc = today.replace(tzinfo = utc)
    # print(today_utc)
    volume_mxn = 0
    78488557
    tickers = ["btc_usd"]
    for ticker in tickers:
        done = False
        cur_marker = None
        while not done:
            trades = api.trades(ticker, limit = 100, sort='desc')
            if cur_marker:
                volume_mxn -= trades[0].price * trade.amount

            for trade in trades:
                if trade.created_at < today 
                #some logic about if trade.created_at < current date - 30 days ago then we break
                #set done = True

                volume_mxn += trade.price * trade.amount
            print(volume_mxn)
            cur_marker = trades[-1].tid

    trades = api.trades("btc_usd", marker=None, limit=100, sort='desc')
    # print(trades)
    trade = trades[1]
    print(trade)
    volume_mxn += trade.price * trade.amount
    # trade_time = trade.created_at.replace(tzinfo = utc)
    print(trade.created_at)
    print(today > trade.created_at)

    # listener = BasicBitsoListener()
    # client = Client(listener)
    # channels = ['orders']
    # book = "eth_mxn"
    # client.connect(channels, book)
    
















    

