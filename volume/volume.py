from api_callling.api_calling import APICall
from dataframe.dataframe import GetDataframe
from real_time_data import RealTimeData
from playsound import playsound


class Volume(GetDataframe):
    def data_pull(self, symbol, look_back):
        days_panda_data = self.get_minute_data(symbol, 1, look_back)
        # close_column = days_panda_data
        volume_column = days_panda_data['Volume']
        return volume_column


def volume_decision(symbol):
    good_volume = True
    while good_volume:
        RealTimeData().streamKline(currency=symbol.lower(), interval="1m")
        current_price = float(RealTimeData.append_currency[-1])
        # print(current_price)
        volume = Volume().data_pull(symbol, 2)
        # # print(volume)
        # avg_price = APICall.client.get_avg_price(symbol=symbol)
        # print(avg_price['price'])
        # currant_price = float(avg_price['price'])
        # # currant_price = 21000
        # print(currant_price)
        first_volume_usd = current_price * volume[0]
        # print(first_volume_usd)
        last_volume_usd = current_price * volume[-1]
        # print(last_volume_usd)

        if first_volume_usd * 10 < last_volume_usd:
            print(f"Current volume {last_volume_usd} is Big volume")
            playsound('Sample.wav')
            good_volume = False
        else:
            print(f"Current volume {last_volume_usd} is smaller than last volume {first_volume_usd} .")


volume_decision("BTCBUSD")
