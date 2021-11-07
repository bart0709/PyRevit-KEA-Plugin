import mysql.connector
import json

"""
host="localhost"
user="root"
password=""
database="plugin"
"""
class Database:

    def __init__(self, host="localhost", user="root", password="", database="kea_plugin"):
        self.mydb = mysql.connector.connect(host=host,user=user,password=password, database=database)
        self.mycursor = mydb.cursor()
    
    def select(self, table, rows):
        sql = "SELECT () FROM ({})".format(rows, table)
        self.mycursor.execute(sql)
        self.mydb.commit()

    def insert(self, table, columns, val) :
        sql = "INSERT INTO {} ({}) VALUES (%s, %s)".format(table, columns)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()
