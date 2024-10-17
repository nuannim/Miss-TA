from Grade import *
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

