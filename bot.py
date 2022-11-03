from pprint import pprint

import talib
from dataframe.dataframe import GetDataframe
from sound.ringbell import Ring
from binance.helpers import round_step_size


class Feature(GetDataframe):
    def data_pull(self, symbol, look_back):
        days_panda_data = self.get_minute_data(symbol, 1, look_back)
        close_column = days_panda_data['Close']
        # minute_panda_data = self.get_minute_data(symbol, 5, look_back)
        # close_column = minute_panda_data['Close']
        return close_column

    def moving_average(self, symbol, look_back):
        close_column = self.data_pull(symbol, look_back)
        real = talib.MA(close_column, timeperiod=int(look_back), matype=0).iloc[-1]
        # print(real)
        return real

    def buy_futures_contract(self, symbol):
        buy = input("Type 'Yes' :")
        print(buy)
        if buy == "Yes":
            APICall.client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def sell_futures_contract(self, symbol):
        sell = input("Type 'Yes' :")
        print(sell)
        if sell == "Yes":
            APICall.client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def buying_signal(self, symbol):
        if self.moving_average(symbol, "99") > self.moving_average(symbol, "25") > self.moving_average(symbol, "7"):
            print(f"Buy/Long : {symbol}")
            self.buy_futures_contract(symbol)
            return symbol
        elif self.moving_average(symbol, "99") < self.moving_average(symbol, "25") < self.moving_average(symbol, "7"):
            print(f"Sell/Short : {symbol}")
            self.sell_futures_contract(symbol)
            return symbol
        else:
            print(f"Asset {symbol} have no position for Buy/Sell")


import pandas as pd
from api_callling.api_calling import APICall


from get_symbol.find_symbols import FindSymbols
fs = FindSymbols()
feature = Feature()

futures_exchange_info = APICall.client.futures_exchange_info()
trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]
# print(len(trading_pairs))
# print(trading_pairs)
#
# busd_pairs = []
# for symbol in trading_pairs:
#     # print(symbol)
#     if "BUSD" in symbol:
#         # print(symbol)
#         busd_pairs.append(symbol)
#
# print(len(busd_pairs))
# print(busd_pairs)
# print(input("stop :"))
#
# busd_pairs = []
# for symbol in trading_pairs:
#     # print(symbol)
#     if "USDT" in symbol:
#         # print(symbol)
#         pass
#     else:
#         busd_pairs.append(symbol)
#
# print(len(busd_pairs))
# print(busd_pairs)
# print(input("stop :"))


def feature_coin_buying_signal():
    ticker_info = pd.DataFrame(APICall.client.get_ticker())
    all_symbol = fs.get_all_symbols("BUSD", ticker_info)
    print(all_symbol)
    busd_pairs = []
    for symbol in all_symbol["symbol"]:
        # print(symbol)
        string = symbol
        result = [word for word in trading_pairs if word in string]
        busd_pairs.append(result)
        if len(result) != 0:
            busd_pairs.append(result)
            feature.buying_signal(symbol)

    print(busd_pairs)

    # print(input("stop :"))


busd_symbol = ['BTCBUSD', 'ETHBUSD', 'BNBBUSD', 'ADABUSD', 'XRPBUSD', 'DOGEBUSD', 'SOLBUSD', 'FTTBUSD', 'AVAXBUSD', 'NEARBUSD', 'GMTBUSD', 'APEBUSD', 'GALBUSD', 'FTMBUSD', 'DODOBUSD', 'ANCBUSD', 'GALABUSD', 'TRXBUSD', 'DOTBUSD', 'TLMBUSD', 'ICPBUSD', 'WAVESBUSD', 'LINKBUSD', 'SANDBUSD', 'LTCBUSD', 'MATICBUSD', 'CVXBUSD', 'FILBUSD', 'LEVERBUSD', 'ETCBUSD', 'LDOBUSD', 'UNIBUSD', 'AUCTIONBUSD', 'AMBBUSD', 'PHBBUSD', 'APTBUSD']
print(f"BUSD pairs we will buy : {len(busd_symbol)}")


def feature_signal():
    for symbol in busd_symbol:
        feature.buying_signal(symbol)


# feature_coin_buying_signal()
ticker_info = pd.DataFrame(APICall.client.get_ticker())
all_symbol = fs.get_all_symbols("BUSD", ticker_info)
# print(all_symbol["symbol"])
print(f"All future symbol : {len(all_symbol['symbol'])}")

feature_signal()

