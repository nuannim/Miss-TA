from StudentModel import *
from CourseModel import *
from Database import *
from Requirement import *
from Grade import *
class StudentCourseController:
    def __init__(self,studentId):
        self.studentId = studentId
        self.Courses = [CourseModel]
        self.Student = StudentModel()
        self.db = MySQLDatabase()


    
    def getCourseForStudent(self):
        self.db.connect()
        query = "SELECT course_history_id FROM course_history"
        result = self.db.fetch_data(query)  # ส่งค่า id เป็น tuple
        self.db.close()
        if result:
            for i in result:
                course = CourseModel()
                course.getDataFromDB(i['course_history_id'])
                self.Courses.append(course)
        return self.Courses

    def setStudentInfo(self):
        self.Student.getDataFromDB(self.studentId)

    def checkstatus(self, cid):
        # ดึงข้อมูลเกรดทั้งหมดของ Student
        grades = self.Student.getspecGrade(cid)
        id_list = []  # สร้าง list เพื่อเก็บ course_id ทั้งหมด
        cyear = 0
        for i in self.Courses:
            if i.getCourseID == cid:
                cyear = i.getYear
        # ดึงค่า year และจำนวน TA ของ Student
        year = self.Student.getYear()
        ta = self.Student.getnum_ta()

        # ตรวจสอบเงื่อนไขเพิ่มเติม
        if int(grades) >= 3 and year >= cyear and ta != 2:
            return True
        else:
            return False

        
