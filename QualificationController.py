from StudentModel import *
from CourseModel import *
from Database import *
class getInfoFromDB:
    def __init__(self,studentId,num):
        self.studentId = studentId
        self.Course = [CourseModel() for _ in range(num)]
        self.Student = StudentModel()
        self.db = MySQLDatabase()

    def getNumOfCourse(self):
        self.db.connect()
        query = "select count(course_id) from course"
        num = self.db.fetch_data(query)
        return num
        

    def setStudentModel(self):
        self.Student.setStudentID
    
    def setCourseModel(self, Id):
        self.Course[Id].setCourseID(Id)
        self.Course[Id].setName(Id)
        self.Course[Id].setReqToFill(Id)
        self.Course[Id].setImage(Id)
        self.Course[Id].setDescription(Id)
        self.Course[Id].setRequirement(Id)
        self.Course[Id].setYear(Id)

        
    # def sendToDatabase():

    # def checkNUll():
    
    # def checkCouse():