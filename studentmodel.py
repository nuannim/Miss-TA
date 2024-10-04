class StudentModel:
    def __init__(self, student_id="", first_name="", last_name="", year=0, announce_list_status=False, waiting_list_status=False, grade=None, wage=0.0):
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._year = year
        self._announce_list_status = announce_list_status
        self._waiting_list_status = waiting_list_status
        self._grade = grade
        self._wage = wage

#^ getter

    def getStudentID(self):
        return self._student_id

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

    def getGrade(self):
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

    def setAnnounceL_Status(self, status):
        self._announce_list_status = status

    def setWaitingL_Status(self, status):
        self._waiting_list_status = status

    def setGrade(self, grade):
        self._grade = grade

    def setWage(self, wage):
        self._wage = wage