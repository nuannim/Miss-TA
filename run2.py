from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *
from ProfessorModel import *

from ProfOperationController import *

def main():

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
    print('======= END run2 =======')

main()

