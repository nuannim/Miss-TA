from datetime import date, datetime

from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *
from ProfessorModel import *

from ProfOperationController import *

def main():

    #* ลองทดสอบ CourseModel() / ProfessorModel() โดยตรง
    oop = CourseModel()
    professorList = ProfessorModel()
    professorList.getDataFromDB(which_id=1)

    print('======= START run2 =======')
    print('--- professorList obj ---')

    print(str(professorList.getFirstName()), 
          str(professorList.getLastName()),
          'num course :', str(professorList.getNumOfCourse()),
          'course id :', str(professorList.getProfCourse()), 
          'profid :', str(professorList.getProfId()))

    print(str(professorList.getProfCourse()))

    print('--- oop obj ---')

    oop.getDataFromDB(102)
    # print(oop.getName())


    oop.setName('test oop')
    oop.setCourseID(9998767)
    oop.setDescription('test send data from python')
    oop.setYear(2023)  # Ensure you set this if it's required
    oop.setAdate(None)  # Ensure correct format
    oop.setWdate(None)  # Ensure correct format
    oop.setCdate(None)  # Ensure correct format
    oop.setQualification_type(1)  # Example value
    oop.setContact(1234567890)  # Example value
    oop.setImage('test_image.png')
    oop.setDataToDB()
    print('======= END  =======')

    #* test ผ่าน ProfOperationController.py
    # oop = CourseModel()
    # allProf = ProfessorModel()
    # controller = ProfOperationController()
    
main()

