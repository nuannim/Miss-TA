from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *
from ProfessorModel import *

from ProfOperationController import *

def main():

    professorList = ProfessorModel()
    professorList.getDataFromDB(which_id=2) #! ทำไม 1 ได้ แต่ 2 ไม่ได้

    print('run2 :', str(professorList.getFirstName()), 
          str(professorList.getLastName()),
          'num course :', str(professorList.getNumOfCourse()),
          'course id', str(professorList.getProfCourse()), 
          'profid :', str(professorList.getProfId()))

    print('run2 : ' + str(professorList.getProfCourse()))
    pass

main()

