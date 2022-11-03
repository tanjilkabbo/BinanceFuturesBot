import talib
from dataframe.dataframe import GetDataframe


class Feature(GetDataframe):
    def data_pull(self, symbol, look_back):
        days_panda_data = self.get_minute_data(symbol, 1, look_back)
        close_column = days_panda_data['Close']
        return close_column

    def moving_average(self, symbol, look_back):
        close_column = self.data_pull(symbol, look_back)
        real = talib.MA(close_column, timeperiod=int(look_back), matype=0).iloc[-1]
        # print(real)
        return real

    def symbol_leverage(self, symbol):
        result = APICall.client.futures_change_leverage(symbol=symbol, leverage=2)
        print(result)
        return symbol

    def buy_futures_contract(self, symbol):
        buy = input("Type 'Y' :")
        print(buy)
        if buy == "Y":
            # self.symbol_leverage(symbol)
            APICall.client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=0.0001)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def sell_futures_contract(self, symbol):
        sell = input("Type 'Y' :")
        print(sell)
        if sell == "Y":
            # self.symbol_leverage(symbol)
            APICall.client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=0.0001)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def big_small_ma(self, symbol):
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

    def rounding(self, num):
        if float(num) > float(10000):
            num = str(num[:(num.find('.'))])
            return num

        elif float(500) < float(num) < float(5000):
            num = str(num[:(num.find('.')+2)])
            return num

        elif float(50) < float(num) < float(500):
            num = str(num[:(num.find('.')+2)])
            return num

        elif float(5) < float(num) < float(50):
            num = str(num[:(num.find('.')+3)])
            return num

        elif float(1) < float(num) < float(5):
            num = str(num[:(num.find('.')+4)])
            return num

        elif float(.5) < float(num) < float(1):
            num = str(num[:(num.find('.')+5)])
            return num

        elif float(.1) < float(num) < float(.5):
            num = str(num[:(num.find('.')+6)])
            return num

    def equal_ma(self, symbol):
        ma_99 = self.moving_average(symbol, "99")
        ma_99 = str(ma_99)
        ma_99 = self.rounding(num=ma_99)

        ma_25 = self.moving_average(symbol, "25")
        ma_25 = str(ma_25)
        ma_25 = self.rounding(num=ma_25)

        ma_07 = self.moving_average(symbol, "7")
        ma_07 = str(ma_07)
        ma_07 = self.rounding(num=ma_07)

        print(f"Asset {symbol} : \n99 MA- {ma_99}\n25 MA- {ma_25}\n07 MA- {ma_07}")

        if ma_99 == ma_25 or ma_25 == ma_07 or ma_99 == ma_07:
            print(f"Buy 'Long'/'Short' quickly : {symbol}")
            self.buy_futures_contract(symbol)
            return symbol

        else:
            print(f"Asset {symbol} have no position for Buy/Sell")

    def buying_signal(self, symbol):
        self.big_small_ma(symbol)
        # self.equal_ma(symbol)
        return symbol



import pandas as pd
from api_callling.api_calling import APICall


from get_symbol.find_symbols import FindSymbols
fs = FindSymbols()
feature = Feature()


busd_symbol = ['BTCBUSD', 'ETHBUSD', 'BNBBUSD', 'ADABUSD', 'XRPBUSD', 'DOGEBUSD', 'SOLBUSD', 'FTTBUSD', 'AVAXBUSD', 'NEARBUSD', 'GMTBUSD', 'APEBUSD', 'GALBUSD', 'FTMBUSD', 'DODOBUSD', 'ANCBUSD', 'GALABUSD', 'TRXBUSD', 'DOTBUSD', 'TLMBUSD', 'ICPBUSD', 'WAVESBUSD', 'LINKBUSD', 'SANDBUSD', 'LTCBUSD', 'MATICBUSD', 'CVXBUSD', 'FILBUSD', 'LEVERBUSD', 'ETCBUSD', 'LDOBUSD', 'UNIBUSD', 'AUCTIONBUSD', 'AMBBUSD', 'PHBBUSD', 'APTBUSD']
print(f"In 'BUSD' pairs we are finding : {len(busd_symbol)} Asset")


def feature_signal():
    for symbol in busd_symbol:
        feature.buying_signal(symbol)


feature_signal()

