from Database import *

class generalController:
    def __init__(self):
        self.db = MySQLDatabase()

    def getNumOfCourse(self):
        self.db.connect()
        query = "SELECT COUNT(course_id) AS course_count FROM course"
        num = self.db.fetch_data(query)
        self.db.close()
        # Assuming fetch_data returns a list of dictionaries
        if num:
            return num[0]['course_count']  # ดึงค่า course_count จากผลลัพธ์
        return 0  # ถ้าไม่มีข้อมูล
    
    def checkstatus(self, sid,cid,cyear):
        grade = self.db.getStudentgrade(sid,cid)
        year = self.db.getYearStudent(sid)
        ta = self.db.getNumTa(sid)

        if int(grade) >= 3 and year >= cyear and ta != 2:
            return True
        else:
            return False
    def getnamecourse(self,id):
        return self.db.getCourseName(id)
    
