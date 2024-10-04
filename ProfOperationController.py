from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *

class ProfOperationController:
    # pCourse = ProfCourseView()
    # pCourseAddEdit = ProfCourseAddnEditView()
    # course = CourseModel()

    def __init__(self, pCourse, pCourseAddEdit, course):
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

        self.pCourse = pCourse
        self.pCourseAddEdit = pCourseAddEdit
        self.course = course


    def nullCheck(self):
        pass

    def sendToDatabase(self, 
                       course : CourseModel = None,
                       pCourse : ProfCourseView = None):

        course.setName(pCourse.getcName)
        course.setCourseID(pCourse.getcID)
        course.setDescription(pCourse.getdesc)
        course.setImage(pCourse.getimage)
        course.setRequirement(pCourse.getreq)
        course.setReqToFill(pCourse.getreq_to_fill)
        course.setAdate(pCourse.getadate)
        course.setWdate(pCourse.getwdate)
        course.setCdate(pCourse.getcdate)
        course.setQualification_type(pCourse.getqtype)
        course.setContact(pCourse.getcontact)

        print("send to database succesfully")

        

    def getInfoFromDatabase(self,
                            course : CourseModel = None, 
                            pCourse : ProfCourseView = None): # get course from db
        
        pass

    def popUp(self):
        pass

    def calculateTA(self):
        pass

    def delete(self):
        pass

