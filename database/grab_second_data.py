"""
Get CSV Data : https://www.cryptodatadownload.com/data/binance/
"""
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

database = r"../database/cripto.db"

# create a database connection
conn = create_connection(database)
with conn:
    print("Write Panda Data here")
