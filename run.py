from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *

from ProfOperationController import *

def main():
    pCourse = ProfCourseView(cName="ISAD", cID=666666, desc="test")
    pCourseAddEdit = ProfCourseAddnEditView()

    allCourse = CourseModel()

    controller = ProfOperationController(pCourse, pCourseAddEdit, allCourse)
    controller.sendToDatabase(allCourse, pCourse)

    


main()