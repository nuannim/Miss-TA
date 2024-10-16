from StudentModel import *
from CourseModel import *
from Database import *
class CourseController:
    def __init__(self,studentId,num):
        self.studentId = studentId
        self.Course = [CourseModel() for _ in range(num)]
        self.Student = StudentModel()
        self.db = MySQLDatabase()

    
    def setCourseModel(self, Id):
        self.Course[Id].setCourseID(self.db.getCourseId(Id))
        self.Course[Id].setName(self.db.getCourseName(Id))
        self.Course[Id].setImage(Id)
        self.Course[Id].setDescription(self.db.getCourseDes(Id))
        self.Course[Id].setRequirement(Id)
        self.Course[Id].setYear(self.db.getCourseYear(Id))

        
    # def sendToDatabase():

    # def checkNUll():
    
    # def checkCouse():
