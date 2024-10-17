from StudentModel import *
from CourseModel import *
from Database import *
from Requirement import *
from Grade import *
class StudentCourseController:
    def __init__(self,studentId):
        self.studentId = studentId
        self.Courses = []
        self.Student = StudentModel()
        self.db = MySQLDatabase()
        self.setStudentInfo()

    
    def getCourseForStudent(self):
        self.db.connect()
        query = "SELECT course_id, name, YEAR, description, image, adate, wdate, cdate, contract FROM course"
        result = self.db.fetch_data(query, (id,))  # ส่งค่า id เป็น tuple
        self.close()
        if result:
            for i in result:
                # return result[0]['course_id']  # ถ้ามีผลลัพธ์ จะคืนค่า course_id ของแถวแรก
                course = CourseModel()
                course.setCourseID(result[i]['course_id'])
                course.setName(result[i]['name'])
                course.setYear(result[i]['YEAR'])
                course.setDescription(result[i]['description'])
                course.setImage(result[i]['image'])
                course.setAdate(result[i]['adate'])
                course.setWdate(result[i]['wdate'])
                course.setCdate(result[i]['cdate'])
                course.setContact(result[i]['contract'])
                status = self.checkstatus(result[i]['course_id'])
                course.setQualification_type(status)
                


                self.db.connect()
                que = "SELECT req_question, required_to_fill FROM prof_req where course_id = %s"
                result2 = self.db.fetch_data(query, (result[i]['course_id'],))  # ส่งค่า id เป็น tuple
                self.close()

                for j in result2:
                    req = Requirement()
                    req.setReq(result2[j]['req_question'])
                    req.setType(result2[j]['required_to_fill'])
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
        self.close()
        self.Student.setStudentID(result[0]['student_id'])
        self.Student.setFirstName(result[0]['firstname'])
        self.Student.setLastName(result[0]['lastname'])
        self.Student.setYear(result[0]['year'])
        self.Student.setnum_ta(result[0]['num_ta'])
        self.db.connect()
        query2 = "SELECT course_id, grade FROM student where student_id = %s"
        result2 = self.db.fetch_data(query2, (self.studentId,))  # ส่งค่า id เป็น tuple
        self.close()
        if result2:
            for i in result2:
                gd = Grade()
                gd.setcourse_id(result2[i]['course_id'])
                gd.setgrade(result2[i]['grade'])
                self.Student.setGrade(gd)

    def checkstatus(self, cid):
        # ดึงข้อมูลเกรดทั้งหมดของ Student
        grades = self.Student.getallGrade()
        id_list = []  # สร้าง list เพื่อเก็บ course_id ทั้งหมด
        grade = None  # เริ่มต้นค่า grade เป็น None

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

        
