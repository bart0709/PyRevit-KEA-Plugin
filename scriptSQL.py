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
    
    #TODO finish this functions, maybe table parameter could be tuple or smth
    def select(self, table, val):
        sql = "SELECT (%s, %s) FROM ({})".format(table)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def insert(self, table, val) :
        sql = "INSERT INTO ({}) VALUES (%s, %s)".format(table)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()
        