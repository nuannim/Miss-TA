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
        self.setStudentInfo()

    
    def getCourseForStudent(self):
        self.db.connect()
        query = "SELECT course_id, name, YEAR, description, image, adate, wdate, cdate, contact FROM course"
        result = self.db.fetch_data(query)  # ส่งค่า id เป็น tuple
        self.db.close()
        if result:
            for i in result:
                course = CourseModel()
                course.setCourseID(i['course_id'])
                course.setName(i['name'])
                course.setYear(i['YEAR'])
                course.setDescription(i['description'])
                course.setImage(i['image'])
                course.setAdate(i['adate'])
                course.setWdate(i['wdate'])
                course.setCdate(i['cdate'])
                course.setContact(i['contact'])
                print(str(i['course_id']) + i['name'] + str(i['YEAR']) + str(i['description']) + str(i['image']) + str(i['adate']) + str(i['wdate']) + str(i['cdate']) + str(i['contact']))
                # status = self.checkstatus(i['course_id'])
                # course.setQualification_type(status)
                


                self.db.connect()
                que = "SELECT req_question, required_to_fill FROM prof_req where course_id = %s"
                result2 = self.db.fetch_data(que, (i['course_id'],))  # ส่งค่า id เป็น tuple
                self.db.close()

                for j in result2:
                    req = Requirement()
                    req.setReq(j['req_question'])
                    req.setType(j['required_to_fill'])
                    course.add_requirement(req)
                
                # status
                
                self.Courses.append(course)
            return self.Courses

        else:
            return None

    def setStudentInfo(self):
        self.db.connect()
        query = "SELECT student_id, firstname, lastname, year, num_ta FROM student where student_id = %s"
        result = self.db.fetch_data(query, (self.studentId,))  # ส่งค่า id เป็น tuple
        self.db.close()
        self.Student.setStudentID(result[0]['student_id'])
        self.Student.setFirstName(result[0]['firstname'])
        self.Student.setLastName(result[0]['lastname'])
        self.Student.setYear(result[0]['year'])
        self.Student.setnum_ta(result[0]['num_ta'])
        self.db.connect()
        query2 = "SELECT course_id, grade FROM student where student_id = %s"
        result2 = self.db.fetch_data(query2, (self.studentId,))  # ส่งค่า id เป็น tuple
        self.db.close()
        if result2:
            for i in result2:
                gd = Grade()
                gd.setcourse_id(i['course_id'])
                gd.setgrade(i['grade'])
                self.Student.setallGrade(gd)

    def checkstatus(self, cid):
        # ดึงข้อมูลเกรดทั้งหมดของ Student
        grades = self.Student.getallGrade()
        id_list = []  # สร้าง list เพื่อเก็บ course_id ทั้งหมด
        grade = None  # เริ่มต้นค่า grade เป็น None
        print("-------grade-------")
        print(grades)
        print("-------grade-------")

        # วน loop ผ่านเกรดทั้งหมด
        for i in grades:
            course_id = i.getcourse_id()
            id_list.append(course_id)
            # ตรวจสอบว่ามี course_id ตรงกับ cid ที่กำหนดหรือไม่
            if course_id == cid:
                grade = i.getgrade()  # ถ้าเจอให้เก็บค่า grade ไว้

        # ถ้า course_id ที่กำหนดไม่อยู่ใน id_list เลย ให้คืนค่า False
        if cid not in id_list:
            return False

        # ดึงค่า year และจำนวน TA ของ Student
        year = self.Student.getYear()
        ta = self.Student.getnum_ta()

        # ตรวจสอบเงื่อนไขเพิ่มเติม
        if grade is not None and int(grade) >= 3 and year >= 3 and ta != 2:
            return True
        else:
            return False

        
