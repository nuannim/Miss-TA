from datetime import date, datetime

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from Database import *

from ProfessorModel import ProfessorModel
from CourseModel import CourseModel

from ProfCourseView import ProfCourseView
from ProfCourseAddnEditView import ProfCourseAddnEditView


class CourseController:
    def __init__(self,
                 db:MySQLDatabase, 
                 app:FastAPI, 
                 template:Jinja2Templates,
                 pModel:ProfessorModel,
                 cModel:CourseModel,
                 pCourseView:ProfCourseView,
                 pCourseAddEditView:ProfCourseAddnEditView):

        self.db = db

        self.app = app
        self.app.mount("/static", StaticFiles(directory='static'), name="static")
        self.template = template

        self.pModel = pModel
        self.cModel = cModel
        self.pCourseView = pCourseView
        self.pCourseAddEditView = pCourseAddEditView

    # ! continue
    #* ต้องถามฟ้อนเรื่อง html
    ################## & app.post() ##################
        # @self.app.post("/test/addcourse", response_class=HTMLResponse)
        @self.app.post("/addcourse", response_class=HTMLResponse)
        async def addcourse_submit(request : Request,
                                name:str=Form(...),
                                course_id:str=Form(...),
                                description:str=Form(...),
                                image:str=Form(...),
                                
                                cdate:date=Form(...),
                                adate:date=Form(...),
                                wdate:datetime=Form(...),
                                qtype:int=Form(...),
                                contact:str=Form(...)
                                    ):
            print()
            print('========= CourseController.py ==========')
            print('name :', name)
            print('course_id :', course_id)
            print('description :', description)
            print('image :', image)
            # print(req)
            print('cdate :', cdate)
            print('adate :', adate)
            print('wdate :', wdate)
            print('qtype :', qtype) # * 1 = อาจารย์ / 0 = ระบบ
            print('contact :', contact)

            cModel.setName(name)
            cModel.setCourseID(course_id)
            cModel.setDescription(description)
            cModel.setImage(image)

            cModel.setCdate(cdate)
            cModel.setAdate(adate)
            cModel.setWdate(wdate)
            cModel.setQualification_type(qtype)
            cModel.setContact(contact)

            cModel.setCourseToDB()
            

            print('===================')
            print()

            #* render same page with @app.get() addcourse()
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )

        #! continue
        # @self.app.post("/test/editcourse")
        @self.app.post("/editcourse")
        async def editcourse_submit():
            pass

    ################## & ##################


########################################################

# from StudentModel import *
# from CourseModel import *
# from Database import *
# class CourseController:
#     def __init__(self,studentId,num):
#         self.studentId = studentId
#         self.Course = [CourseModel() for _ in range(num)]
#         self.Student = StudentModel()
#         self.db = MySQLDatabase()

    
#     def setCourseModel(self, Id):
#         self.Course[Id].setCourseID(self.db.getCourseId(Id))
#         self.Course[Id].setName(self.db.getCourseName(Id))
#         self.Course[Id].setImage(Id)
#         self.Course[Id].setDescription(self.db.getCourseDes(Id))
#         self.Course[Id].setRequirement(Id)
#         self.Course[Id].setYear(self.db.getCourseYear(Id))

        
    # def sendToDatabase():

    # def checkNUll():
    
    # def checkCouse():
