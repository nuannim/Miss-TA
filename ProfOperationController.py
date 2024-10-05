from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *

class ProfOperationController:

    def __init__(self, pCourse, pCourseAddEdit, course):
        self.pCourse = pCourse
        self.pCourseAddEdit = pCourseAddEdit
        self.course = course

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
        
        # pass
### ^

#^ new
    def sendToModel(self, course : CourseModel, 
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

        print("::::: ProfOperationController :: debug :::::\nsent to database successfully")

#* get info from db to ProfCourseView.py
    def getInfoFromModel(self, course : CourseModel = None, #! getInfoFromDatabase() has changed to getInfoFromModel()
                            cView : ProfCourseView = None):
        cView.displayMainCourse(
                                course.getName(),
                                course.getCourseID(),
                                course.getDescription(),
                                course.getImage(),
                                course.getRequirement(),
                                course.getReqToFill(),
                                course.getAdate(),
                                course.getWdate(),
                                course.getCdate(),
                                course.getQualification_type(),
                                course.getContact()
                                )
        
        #return cView.displayMainCourse(
                                # course.getName(),
                                # course.getCourseID(),
                                # course.getDescription(),
                                # course.setImage(),
                                # course.setRequirement(),
                                # course.getReqToFill(),
                                # course.getAdate(),
                                # course.getWdate(),
                                # course.getCdate(),
                                # course.getQualification_type(),
                                # course.getContact()
                                # )

### ^



    def popUp(self):
        pass

    def calculateTA(self):
        pass

    def delete(self):
        pass

