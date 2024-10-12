from Database import *

class ProfessorModel:
    # def __init__(self, first_name="", last_name="", num_of_course=0, course=None, prof_id=""):
    def __init__(self, first_name="", last_name="", num_of_course=0, prof_course=[], prof_id=""):
        self._first_name = first_name
        self._last_name = last_name
        self._num_of_course = num_of_course
        # self._course = course if course is not None else []
        self._prof_course = prof_course
        self._prof_id = prof_id

        self.db = MySQLDatabase()

#^ getter

    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getNumOfCourse(self):
        return self._num_of_course

    # def getCourse(self):
    #     return self._course

    def getProfCourse(self):
        return self._prof_course

    def getProfId(self):
        return self._prof_id

#^ setter

    def setFirstName(self, first_name):
        self._first_name = first_name

    def setLastName(self, last_name):
        self._last_name = last_name

    def setNumOfCourse(self, num_of_course):
        self._num_of_course = num_of_course

    # def setCourse(self, course):
    #     if isinstance(course, list):
    #         self._course = course
    #     else:
    #         self._course = [course]

    def setProfCourse(self, pCourse):
        self._prof_course = pCourse

    def setProfId(self, prof_id):
        self._prof_id = prof_id




#######################################################^
#######################################################^




#^ db getter

    def getDataFromDB(self, which_id):
        '''get data from database then set it into ProfessorModel.py attribute'''
        self.db.connect()

        #* query firstname / lastname
        query = "select * from professor where prof_id = %d" %which_id
        message = self.db.fetch_data(query)
        
        print(message)

        self.setFirstName(message[0]["firstname"])
        self.setLastName(message[0]["lastname"])
        # self.setNumOfCourse(message[which_id-1]["num_of_course"])

        #* query prof_course 
        query_prof_course = 'select course_id from prof_course where prof_id = %d' %which_id
        prof_course_message = self.db.fetch_data(query_prof_course)

        courselist = [i["course_id"] for i in prof_course_message]
        
        # print(courselist)
        self.setProfCourse(courselist)
        # print(prof_course_message[0:]["course_id"])
        # self.setProfCourse(prof_course_message[which_id-1]["course_id"])

        # self.setProfCourse(message)

        #* set num_of_course
        self.setNumOfCourse(len(courselist))

        #* query prof_id
        self.setProfId(which_id)

#^ db setter

    def setDataToDB(self):
        '''ยังไม่ได้ทำ'''
        pass
