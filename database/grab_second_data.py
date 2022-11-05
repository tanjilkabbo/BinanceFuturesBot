"""
Get CSV Data : https://www.cryptodatadownload.com/data/binance/
"""
import sqlite3

from dataframe.dataframe import GetDataframe

total_years = 1
months = 1 * total_years
days = 1 * months
hours = 24 * days
minute = hours * 60
print(minute)
time_of_data = int(minute)


data = GetDataframe().get_minute_data("BTCBUSD", 1, time_of_data)
# print(data["Open"])
open_data = data["Open"]
for data in open_data:
    print(data)

    connection = sqlite3.connect("../database/cripto.db")
    cur = connection.cursor()

    print(cur)

    cur.execute(
        "INSERT INTO btcbusd VALUES (:id, :symbol, :Open, :High, :Low,  :Close,:Volume, :Change , :Time)",
        {
            'id': None,
            'symbol': "ETHBUSD",
            'Open': data,
            'High': None,
            'Low': None,
            'Close': None,
            'Volume': None,
            'Change': None,
            'Time': None
        })

    connection.commit()
    cur.close()

