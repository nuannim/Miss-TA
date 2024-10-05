from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *

from ProfOperationController import *

def main():
    # pCourse = ProfCourseView(cName="ISAD", cID=666666, desc="test")
    # pCourseAddEdit = ProfCourseAddnEditView()

    # allCourse = CourseModel()

    # controller = ProfOperationController(pCourse, pCourseAddEdit, allCourse)
    # controller.sendToDatabase(allCourse, pCourse)

    isadView = ProfCourseView()
    isadAddEditView = ProfCourseAddnEditView()
    isadCourse = CourseModel()

    controller = ProfOperationController(isadView, isadAddEditView, isadCourse)

    controller.sendToModel(
                            isadCourse,
                            cName="ISAD Course",
                            cID=666666,
                            desc="this is about isad ",
                            image=None,
                            req=None,
                            reqToFill=0,
                            adate=16-9-24,
                            wdate=19-9-24,
                            cdate=20-9-24,
                            qtype=0,
                            contact="0800000000"
                            )

    print('isad get name = ' + isadCourse.getName())

    controller.getInfoFromModel(isadCourse, isadView)

    pass

main()
