from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self):
        #*freesql
        # self.host = "sql12.freesqldatabase.com"
        # self.user = "sql12738833"
        # self.password = "mmeNGlF5xv"
        # self.database = "sql12738833"
        # self.port = "3306"
        # self.connection = None

        # * localhost title
        self.host = "26.64.54.150"
        self.user = "any"
        self.password = "iloveisad"
        self.database = "sql12738833"
        self.port = "3306"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def fetch_data(self, query, params=None):
        cursor = None
        result = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)  # ใช้ parameters แทนการใช้ format()
            result = cursor.fetchall()
        except Error as e:
            print(f"Error while fetching data: {e}")
        finally:
            if cursor:
                cursor.close()
        return result

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

    def insert_data(self, query, params=None):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()  # Committing the transaction
        except Error as e:
            print(f"Error while inserting data: {e}")
        finally:
            if cursor:
                cursor.close()
