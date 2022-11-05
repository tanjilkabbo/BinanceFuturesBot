from api_callling.api_calling import APICall

import pandas as pd

pd.set_option('mode.chained_assignment', None)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class GetDataframe:

    def frame_to_symbol(self, symbol, frame):
        frame = frame.iloc[:, :6]
        if frame.columns.size > 0:
            frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
            frame = frame.set_index('Time')
            frame.index = pd.to_datetime(frame.index, unit='ms')
            frame = frame.astype(float)
            change = ((frame['Close'] - frame['Open']) * 100) / frame['Open']
            frame['Change'] = change
            frame['symbol'] = symbol
            print(frame)
            return frame

    def get_month_data(self, symbol, interval, lookback):
        frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}M", f"{lookback} month ago UTC"))
        frame = self.frame_to_symbol(symbol, frame)
        return frame

    def get_week_data(self, symbol, interval, lookback):
        frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}w", f"{lookback} week ago UTC"))
        frame = self.frame_to_symbol(symbol, frame)
        return frame

    def get_day_data(self, symbol, interval, lookback):
        frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}d", f"{lookback} day ago UTC"))
        frame = self.frame_to_symbol(symbol, frame)
        return frame

    def get_hour_data(self, symbol, interval, lookback):
        frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}h", f"{lookback} hour ago UTC"))
        frame = self.frame_to_symbol(symbol, frame)
        return frame

    def get_minute_data(self, symbol, interval, lookback):
        frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}m", f"{lookback} min ago UTC"))
        frame = self.frame_to_symbol(symbol, frame)

        # try:
        #     frame = pd.DataFrame(APICall.client.get_historical_klines(symbol, f"{interval}m", f"{lookback} min ago UTC"))
        #     frame = self.frame_to_symbol(symbol, frame)
        # except:
        #     print(symbol)
        #     print(input("stop :"))
        #     pass

        # print(frame)
        return frame

    def data_function(self, symbol, interval, lookback):
        return self.get_minute_data(symbol, interval, lookback)


# data_f = GetDataframe()
# print(data_f.data_function('BTCBUSD', 1, 5))

# GetDataframe().get_minute_data('GALABUSD', 1, 90)
