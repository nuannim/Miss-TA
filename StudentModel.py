from Grade import *
from Database import *
class StudentModel:
    def __init__(self, 
                 student_id="", 
                 first_name="", 
                 last_name="", 
                 year=0, 
                 announce_list_status=False, 
                 waiting_list_status=False,  
                 wage=0.0,
                 num_ta = 0):
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._year = year
        self._announce_list_status = announce_list_status
        self._waiting_list_status = waiting_list_status
        self._grade = [Grade]
        self._wage = wage
        self._num_ta = num_ta
        self.db = MySQLDatabase()

#^ getter

    def getStudentID(self):
        return self._student_id
    
    def getnum_ta(self):
        return self._num_ta

    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getYear(self):
        return self._year

    def getAnnounceL_Status(self):
        return self._announce_list_status

    def getWaitingL_Status(self):
        return self._waiting_list_status

    def getallGrade(self):
        return self._grade

    def getspecGrade(self, cid):
        if Grade is None:
            return 0
        else:
            for i in self._grade:
                if isinstance(i, Grade):  
                    if i.getcourse_id() == cid:
                        return i.getgrade()
            return 0 
    
    def getWage(self):
        return self._wage

#^ setter

    def setStudentID(self, student_id):
        self._student_id = student_id

    def setFirstName(self, first_name):
        self._first_name = first_name

    def setLastName(self, last_name):
        self._last_name = last_name

    def setYear(self, year):
        self._year = year

    def setnum_ta(self, num_ta):
        self._num_ta = num_ta

    def setAnnounceL_Status(self, status):
        self._announce_list_status = status

    def setWaitingL_Status(self, status):
        self._waiting_list_status = status

    def setallGrade(self, grade):
        if isinstance(grade, Grade):
            self._grade.append(grade)
        else:
            raise TypeError("ต้องเป็น object ของคลาส grade เท่านั้น")

    def setWage(self, wage):
        self._wage = wage

    def getDataFromDB(self, studentId):
        self.db.connect()
        query = "SELECT student_id, firstname, lastname, year, num_ta FROM student where student_id = %s"
        query2 = "SELECT course_id, grade FROM student where student_id = %s"
        result2 = self.db.fetch_data(query2, (studentId,))  # ส่งค่า id เป็น tuple
        result = self.db.fetch_data(query, (studentId,))  # ส่งค่า id เป็น tuple
        self.db.close()
        self.setStudentID(result[0]['student_id'])
        self.setFirstName(result[0]['firstname'])
        self.setLastName(result[0]['lastname'])
        self.setYear(result[0]['year'])
        self.setnum_ta(result[0]['num_ta'])
        # self.db.connect()
        # query2 = "SELECT course_id, grade FROM student where student_id = %s"
        # result2 = self.db.fetch_data(query2, (self.studentId,))  # ส่งค่า id เป็น tuple
        # self.db.close()
        if result2:
            for i in result2:
                gd = Grade()
                gd.setcourse_id(i['course_id'])
                gd.setgrade(i['grade'])
                self.setallGrade(gd)