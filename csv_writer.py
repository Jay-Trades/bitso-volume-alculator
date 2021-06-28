import sys
import os
import datetime
import time
import pytz

import bitso
import csv

if __name__ == '__main__':
    api = bitso.Api("AVBtwoGxZY", "849ea8d75b88fa08b713841f3b916b90")

    trades = api.trades("btc_usd", marker=None, limit=1, sort='desc')
    timezone = trades[0].created_at.tzinfo  
    print(timezone)
    tz = pytz.timezone("UTC")
    # endDate = datetime.datetime(year = 2019, month = 6, day=1, hour = 0, mintue = 0, second = 0, )
    endDate = datetime.datetime(2019, 6, 1,  0, 0, 0)
    startDate = datetime.datetime(2020, 6, 1,  0, 0, 0)
    ed = tz.localize(endDate)
    ed2 = ed.astimezone(pytz.UTC)
    sd = tz.localize(startDate)
    sd2 = sd.astimezone(pytz.UTC)
    print(sd2.tzinfo)
    print(ed2.tzinfo)
    # tid = "40360294"
    #"15907510"
    tid = "16000000"
    # tid = "15896082" 
    #"15892021"


    hashset = set()
    hashset.add(startDate)
    hashset.add(startDate)
    print(hashset)


    counter = 0
    tickers = ["mana_mxn", "tusd_mxn"]
    #, "btc_usd", "eth_usd", "xrp_usd", "xrp_mxn", "ltc_mxn", "bch_mxn", "bat_mxn", "btc_mxn", "eth_mxn"] 
    
    with open('tusd.csv', mode='w') as trade_file:
        trade_writer = csv.writer(trade_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        trade_writer.writerow(["date", "Trade id", "ticker", "price", "quantity", "total volume", "fees", "fees currency", "side", "oid"])
        for ticker in tickers:
            done = False
            cur_marker = tid
            
            while not done:
                if counter == 300:
                    counter = 0
                    print("sleeping")
                    time.sleep(60)


                trades = api.user_trades(book=ticker, marker = cur_marker, limit = 100, sort='desc')
                # print(trades)
                if not trades:
                    done = True

                for trade in trades:
                    if trade.created_at < ed2:
                        done = True
                        print("LAST TRADE (not in time frame) CREATED DATE ---------- ")
                        print(trade.created_at)
                        print(trade)
                        break
                    else:
                        trade_writer.writerow([trade.created_at, trade.tid, trade.book, trade.price, trade.major, trade.minor, trade.fees_amount, trade.fees_currency, trade.side, trade.oid])

                cur_marker = trade.tid
                counter += 1
                print(trade.created_at)
                print(counter)


    # for ticker in tickers:
    #     done = False
    #     cur_marker = None
    #     while not done:
    #         if cur_marker:
    #             trades = api.user_trades(book=ticker, marker = tid, limit = 100, sort='desc')
    #         else:
    #             trades = api.user_trades(book=ticker, limit = 100, sort='desc')
    #             # print(trades[0])
    #             # print(trades[0].created_at)
    #             print(ticker)

    #         for trade in trades:
    #             if trade.created_at < sd2:
    #             #some logic about if trade.created_at < current date - 30 days ago 
    #                 done = True
    #                 print("LAST TRADE (not in time frame) CREATED DATE ____")
    #                 print(trade.created_at)
    #                 print(trade)
    #                 break

    #         cur_marker = trade.tid