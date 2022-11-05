"""
Base on https://www.sqlitetutorial.net/sqlite-python/
"""
import sqlite3
from sqlite3 import Error


class Connection:
    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main(self):
        database = r"../database/cripto.db"

        sql_create_btcbusd_table = """ CREATE TABLE IF NOT EXISTS btcbusd (
                                            id integer PRIMARY KEY,
                                            symbol text NOT NULL,
                                            Open text,
                                            High text,
                                            Low text,
                                            Close text,
                                            Volume text,
                                            Change text,
                                            Time text
                                        ); """

        # create a database connection
        conn = self.create_connection(database)

        # create tables
        if conn is not None:
            # create projects table
            self.create_table(conn, sql_create_btcbusd_table)



        else:
            print("Error! cannot create the database connection.")


if __name__ == '__main__':
    Connection().main()
