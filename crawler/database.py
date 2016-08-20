# -*- coding: utf8 -*-

import MySQLdb
import datetime
import warnings

warnings.filterwarnings("ignore")

class database:
    database = ""
    table = ""

    def connect_database(self, database_name):
        database = database_name
        print("database %s connecting" % database_name)
        self.__db = MySQLdb.connect(host = "localhost", user = "root", passwd="kaozijicx", charset = "utf8")
        self.__cursor = self.__db.cursor()

        sql = "CREATE DATABASE IF NOT EXISTS %s" % database_name
        self.__cursor.execute(sql)

        self.close_database()

        self.__db = MySQLdb.connect(host = "localhost", user = "root", passwd="kaozijicx", db = database_name, charset = "utf8")
        self.__cursor = self.__db.cursor()
        print("database %s connected" % database_name)

    def create_table(self, table_name):
        talbe = table_name
        print("table %s creating" % table_name)
        self.__cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
        sql = "CREATE TABLE %s (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20))" % table_name
        self.__cursor.execute(sql)
        print("table %s created" % table_name)

    def close_database(self):
        self.__cursor.close()
        self.__db.close()


x = database()
x.connect_database("CX")
x.create_table("CX")
