"""
Get CSV Data : https://www.cryptodatadownload.com/data/binance/
"""

import sqlite3
from datetime import datetime

import pandas as pd

from pandas import Timestamp


from database.connection import create_connection

from dataframe.dataframe import GetDataframe

total_years = 1
months = 1 * total_years
days = 1 * months
hours = 24 * days
minute = hours * 60
print(minute)
time_of_data = int(minute)


data = GetDataframe().get_minute_data("BTCBUSD", 1, time_of_data)
print(data)

for i in range(len(data)):
    # print(single_data)
    open_position = data['Open'].iloc[i]
    high_position = data['High'].iloc[i]
    low_position = data['Low'].iloc[i]
    close_position = data['Close'].iloc[i]
    volume_position = data['Volume'].iloc[i]
    change_position = data['Change'].iloc[i]
    symbol_position = data['symbol'].iloc[i]
    time_position = data.index[i]
    unix_time = time_position.timestamp()
    print(f"{open_position}, {high_position}, {low_position}, {close_position}, {volume_position}, {change_position}, {symbol_position} , {time_position}, {unix_time}")

    connection = sqlite3.connect("../database/cripto.db")
    cur = connection.cursor()

    # print(cur)

    cur.execute(
        "INSERT INTO btcbusd VALUES (:id, :symbol, :Open, :High, :Low,  :Close,:Volume, :Change , :Time)",
        {
            'id': None,
            'symbol': symbol_position,
            'Open': open_position,
            'High': high_position,
            'Low': low_position,
            'Close': close_position,
            'Volume': volume_position,
            'Change': change_position,
            'Time': unix_time
        })

    connection.commit()
    cur.close()


