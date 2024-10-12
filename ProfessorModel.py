from Database import *

class ProfessorModel:
    def __init__(self, first_name="", last_name="", num_of_course=0, course=None, prof_id=""):
        self._first_name = first_name
        self._last_name = last_name
        self._num_of_course = num_of_course
        self._course = course if course is not None else []
        self._prof_id = prof_id

        self.db = MySQLDatabase()

#^ getter

    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getNumOfCourse(self):
        return self._num_of_course

    def getCourse(self):
        return self._course

    def getProfId(self):
        return self._prof_id

#^ setter

    def setFirstName(self, first_name):
        self._first_name = first_name

    def setLastName(self, last_name):
        self._last_name = last_name

    def setNumOfCourse(self, num_of_course):
        self._num_of_course = num_of_course

    def setCourse(self, course):
        if isinstance(course, list):
            self._course = course
        else:
            self._course = [course]

    def setProfId(self, prof_id):
        self._prof_id = prof_id


#^ db getter
    def getAllDataFromDB(self):
        self.db.connect()
        query = "select "
        pass

#^ db setter
    def setDataToDB(self):
        pass