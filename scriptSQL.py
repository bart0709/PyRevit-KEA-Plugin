import mysql.connector

"""
host="localhost"
user="root"
password=""
database="plugin"
"""
class Database:

    def __init__(self, host="localhost", user="root", password="", database="plugin"):
        self.mydb = mysql.connector.connect(host=host,user=user,password=password, database=database)
        self.mycursor = self.mydb.cursor()
    
    def select(self, table, rows):
        sql = "SELECT () FROM ({})".format(rows, table)
        self.mycursor.execute(sql)
        self.mydb.commit()
        return self.mycursor.fetchall()

    def insert(self, table, columns, val) :
        sql = "INSERT INTO {} ({}) VALUES (%s, %s)".format(table, columns)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def update(self, table, column1, column2, condition, val) :
        sql = "UPDATE {} SET {} = {} WHERE {} = {}".format(table, column1, val, column2, condition)
        self.mycursor.execute(sql)
        self.mydb.commit()
        return self.mycursor.fetchall()
