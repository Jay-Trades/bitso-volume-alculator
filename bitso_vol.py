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
import datetime
import pytz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##


from bitso import Client, Listener
import bitso

utc=pytz.UTC

        
if __name__ == '__main__':
    api = bitso.Api("AVBtwoGxZY", "849ea8d75b88fa08b713841f3b916b90")
    # status = api.account_status()
    # balance = api.balances()
    # print(status)
    # print (dir(balance))
    
    trades = api.trades("btc_usd", marker=None, limit=1, sort='desc')
    timezone = trades[0].created_at.tzinfo

    timePeriod = int(input("Enter number of days you want the volume for: "))
    old_day = datetime.datetime.now(timezone) - datetime.timedelta(timePeriod)
    # hour = int(input("Enter number of hours on top of the date: "))
    # old_day = old_day - datetime.timedelta(hours= hour)
    # print(old_day)

    first_six_hours = old_day - datetime.timedelta(hours= 18)
    second_six_hours = old_day - datetime.timedelta(hours= 12)
    third_six_hours = old_day - datetime.timedelta(hours= 6)



    tickers = ["mana_mxn", "xrp_mxn", "ltc_mxn", "bch_mxn", "bat_mxn", "btc_mxn", "eth_mxn"] 
    # max 30000 trades in a mintue 300 api call * 100 per 
    vol = {}
    for ticker in tickers:
        done = False
        cur_marker = None
        second, third, last = (True,) * 3
        volume_mxn = 0
        while not done:
            if cur_marker:
                trades = api.user_trades(book=ticker, marker = cur_marker, limit = 100, sort='desc')
            else:
                trades = api.user_trades(book = ticker, limit = 100, sort='desc')
                # print(trades[0])
                # print(trades[0].created_at)
                print(ticker)

            for trade in trades:

                if trade.created_at < old_day:
                    if last:
                        if 4 in vol:
                            vol[4] += volume_mxn
                        else:
                            vol[4] = volume_mxn
                        last = False

                if trade.created_at < third_six_hours:
                    if third:
                        if 3 in vol:    
                            vol[3] += volume_mxn
                        else:
                            vol[3] = volume_mxn
                        third = False

                if trade.created_at < second_six_hours:
                    if second:
                        if 2 in vol:
                            vol[2] += volume_mxn
                        else:
                            vol[2] = volume_mxn
                        second = False

                if trade.created_at < first_six_hours:
                    done = True
                    print("LAST TRADE (not in time frame) CREATED DATE: " + str(trade.created_at))
                    if 1 in vol:
                        vol[1] += volume_mxn
                    else:
                        vol[1] = volume_mxn
                    break
                
                volume_mxn += abs(trade.minor)


            cur_marker = trade.tid
            # print(volume_mxn)
            # print(counter)
    print(str(timePeriod) + " Day: " + str(vol[4]))
    print("Day + 6 hours: " + str(vol[3]))
    print("Day + 12 hours: " + str(vol[2]))
    print("Day + 16 hours: " + str(vol[1]))


    
    # trades = api.trades("btc_usd", marker=None, limit=100, sort='desc')
    # print(trades)
    # trade = trades[1]
    # print(trade)
    # volume_mxn += trade.price * trade.amount
    # # trade_time = trade.created_at.replace(tzinfo = utc)
    # print(trade.created_at)
    # print(today > trade.created_at)

    
















    

