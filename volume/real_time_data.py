import websocket

import json


class RealTimeData:
    append_currency = []

    def on_message(self, ws, message):
        json_message = json.loads(message)
        current_data = json_message["k"]["c"]
        RealTimeData.append_currency.append(current_data)
        # print(current_data)
        ws.close()

    def on_error(self, ws, error):
        print(error)

    def on_close(self, close_msg):
        print("### closed ###" + close_msg)

    def streamKline(self, currency, interval):
        websocket.enableTrace(False)
        socket = f'wss://stream.binance.com:9443/ws/{currency}@kline_{interval}'
        ws = websocket.WebSocketApp(socket,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close
                                    )

        ws.run_forever()


# rt = RealTimeData()
# print(rt.append_currency)
