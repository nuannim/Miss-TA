
from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self):
        self.host = "sql12.freesqldatabase.com"
        self.user = "sql12737141"
        self.password = "J4SDu1KBvf"
        self.database = "sql12737141"
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

    def getCourseId(self, id):
        self.connect()
        query = "SELECT course_id FROM course WHERE id = %s"
        result = self.fetch_data(query, (id,))  # ส่งค่า id เป็น tuple
        self.close()
        if result:
            return result[0]['course_id']  # ถ้ามีผลลัพธ์ จะคืนค่า course_id ของแถวแรก
        return None  # ถ้าไม่พบข้อมูลใด ๆ

    def getCourseName(self, id):
        self.connect()
        query = "SELECT name FROM course WHERE id = %s"
        result = self.fetch_data(query, (id,))  # ส่งค่า id เป็น tuple
        self.close()
        if result:
            return result[0]['name']
        return None  # ถ้าไม่พบข้อมูลใด ๆ

    def getCourseDes(self, id):
        self.connect()
        query = "SELECT description FROM course WHERE id = %s"
        result = self.fetch_data(query, (id,))  # ส่งค่า id เป็น tuple
        self.close()
        if result:
            return result[0]['description']
        return None  # ถ้าไม่พบข้อมูลใด ๆ

    def getStudentgrade(self, sid, cid):
        self.connect()
        query = "SELECT grade FROM grade WHERE student_id = %s AND course_id = %s"
        result = self.fetch_data(query, (sid, cid))  # ส่งค่า sid และ cid เป็น tuple
        self.close()
        if result:
            return result[0]['grade']  # ถ้ามีผลลัพธ์ ให้คืนค่าผลลัพธ์
        return None  # ถ้าไม่พบข้อมูล
    
    def getYearStudent(self,id):
        self.connect()
        query = "select year from student where student_id = %s"
        result = self.fetch_data(query,(id,))
        self.close()
        if result:
            return result[0]['year']  # ถ้ามีผลลัพธ์ ให้คืนค่าผลลัพธ์
        return None  # ถ้าไม่พบข้อมูล
    
    def getNumTa(self,id):
        self.connect()
        query = "select num_ta from student where student_id = %s"
        result = self.fetch_data(query,(id,))
        self.close()
        if result:
            return result[0]['num_ta']  # ถ้ามีผลลัพธ์ ให้คืนค่าผลลัพธ์
        return None  # ถ้าไม่พบข้อมูล
    
    def getCourseYear(self, id):
        self.connect()
        query = "SELECT year FROM course WHERE id = %s"
        result = self.fetch_data(query, (id,))  # ส่งค่า id เป็น tuple
        self.close()
        if result:
            return result[0]['year']
        return None  # ถ้าไม่พบข้อมูลใด ๆ

#^ ##############################################

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
