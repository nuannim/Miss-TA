from ProfCourseView import *
from ProfCourseAddnEditView import *

from CourseModel import *       #* done
from ProfessorModel import *    #* done

#! เขียนตอนเชื่อม front เสร็จแล้ว
class ProfOperationController:
    def __init__(self):
        pass
# class ProfOperationController:
#     def __init__(self, 
#                  pCourseV : ProfCourseView, 
#                  pCourseAddEditV : ProfCourseAddnEditView, 
#                  course : CourseModel,
#                  ):
#         self.pCourseV = pCourseV
#         self.pCourseAddEditV = pCourseAddEditV
#         self.course = course

#     def getInfoFromDisplay():
#         pass


#     def nullCheck(self):
#         pass

#     def sendToModel(self, course : CourseModel, 
#                        cName, cID, desc, image, req, reqToFill, adate, wdate, cdate, qtype, contact):
#         course.setName(cName)
#         course.setCourseID(cID)
#         course.setDescription(desc)
#         course.setImage(image)
#         course.setRequirement(req)
#         course.setReqToFill(reqToFill)
#         course.setAdate(adate)
#         course.setWdate(wdate)
#         course.setCdate(cdate)
#         course.setQualification_type(qtype)
#         course.setContact(contact)

#         print("::::: ProfOperationController :: debug :::::\nsent to database successfully")

# #* get info from db to ProfCourseView.py
#     def getInfoFromModel(self, course : CourseModel = None, #! getInfoFromDatabase() has changed to getInfoFromModel()
#                             cView : ProfCourseView = None):
#         cView.displayMainCourse(
#                                 course.getName(),
#                                 course.getCourseID(),
#                                 course.getDescription(),
#                                 course.getImage(),
#                                 course.getRequirement(),
#                                 course.getReqToFill(),
#                                 course.getAdate(),
#                                 course.getWdate(),
#                                 course.getCdate(),
#                                 course.getQualification_type(),
#                                 course.getContact()
#                                 )
        
#         #return cView.displayMainCourse(
#                                 # course.getName(),
#                                 # course.getCourseID(),
#                                 # course.getDescription(),
#                                 # course.setImage(),
#                                 # course.setRequirement(),
#                                 # course.getReqToFill(),
#                                 # course.getAdate(),
#                                 # course.getWdate(),
#                                 # course.getCdate(),
#                                 # course.getQualification_type(),
#                                 # course.getContact()
#                                 # )

#     def popUp(self):
#         pass

#     def calculateTA(self):
#         pass

#     def delete(self):
#         pass

