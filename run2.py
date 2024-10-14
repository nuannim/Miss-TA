from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *
from ProfessorModel import *

from ProfOperationController import *

def main():

    #* ลองทดสอบ CourseModel() / ProfessorModel() โดยตรง
    # oop = CourseModel()
    # professorList = ProfessorModel()
    # professorList.getDataFromDB(which_id=1)

    # print('======= START run2 =======')
    # print('--- professorList obj ---')

    # print(str(professorList.getFirstName()), 
    #       str(professorList.getLastName()),
    #       'num course :', str(professorList.getNumOfCourse()),
    #       'course id :', str(professorList.getProfCourse()), 
    #       'profid :', str(professorList.getProfId()))

    # print(str(professorList.getProfCourse()))

    # print('--- oop obj ---')

    # oop.getDataFromDB(102)
    # # print(oop.getName())
    # print('======= END  =======')

    #* test ผ่าน ProfOperationController.py
    oop = CourseModel()
    allProf = ProfessorModel()
    controller = ProfOperationController()
    
main()

