from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *

class ProfOperationController:

    def __init__(self, pCourse, pCourseAddEdit, course):
        self.pCourse = pCourse
        self.pCourseAddEdit = pCourseAddEdit
        self.course = course

        # self.cName = None
        # self.cID = None
        # self.desc = None
        # self.image = None
        # self.req = None
        # self.req_to_fill = None
        # self.adate = None
        # self.wdate = None
        # self.cdate = None
        # self.qtype = None
        # self.contact = None

    def getInfoFromDisplay():
        pass


    def nullCheck(self):
        pass

#^ old
    # def sendToDatabase(self, 
    #                    course : CourseModel = None,
    #                    pCourse : ProfCourseView = None):

    #     course.setName(pCourse.getcName())
    #     course.setCourseID(pCourse.getcID())
    #     course.setDescription(pCourse.getdesc())
    #     course.setImage(pCourse.getimage())
    #     course.setRequirement(pCourse.getreq())
    #     course.setReqToFill(pCourse.getreq_to_fill())
    #     course.setAdate(pCourse.getadate())
    #     course.setWdate(pCourse.getwdate())
    #     course.setCdate(pCourse.getcdate())
    #     course.setQualification_type(pCourse.getqtype())
    #     course.setContact(pCourse.getcontact())

    #     print("send to database succesfully")

    # def getInfoFromDatabase(self,
    #                         course : CourseModel = None, 
    #                         pCourse : ProfCourseView = None): # get course from db
        
        pass
### ^

#^ new
    def sendToDatabase(self, course : CourseModel, 
                       cName, cID, desc, image, req, reqToFill, adate, wdate, cdate, qtype, contact):
        course.setName(cName)
        course.setCourseID(cID)
        course.setDescription(desc)
        course.setImage(image)
        course.setRequirement(req)
        course.setReqToFill(reqToFill)
        course.setAdate(adate)
        course.setWdate(wdate)
        course.setCdate(cdate)
        course.setQualification_type(qtype)
        course.setContact(contact)

    def getInfoFromDatabase(self, course : CourseModel = None, 
                            cView : ProfCourseView = None): # get course from db
        return cView.displayMainCourse(course.getName(), ...)


### ^



    def popUp(self):
        pass

    def calculateTA(self):
        pass

    def delete(self):
        pass

