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

    #! เหลือ req
    ################## & app.post() ##################
        # @self.app.post("/test/addcourse", response_class=HTMLResponse)
        @self.app.post("/addcourse", response_class=HTMLResponse)
        async def addcourse_submit(request : Request,
                                name:str=Form(...),
                                course_id:str=Form(...),
                                description:str=Form(...),
                                image:str=Form(...),
                                req:list[str] = Form(...),
                                cdate:date=Form(...),
                                adate:date=Form(...),
                                wdate:datetime=Form(...),
                                qtype:int=Form(...),
                                contact:str=Form(...),
                                ta_type:str=Form(...),
                                an_type:str=Form(...),
                                year:str=Form(...),
                                enroll_num:str=Form(...),
                                num_regis:str=Form(...)
                                    ):
            print()
            print('========= CourseController.py - @app.post("/addcourse") ==========')
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

            print()
            print('ta_type :', ta_type)
            print('an_type :', an_type)
            print('year :', year)
            print('enroll_num :', enroll_num)
            print('num_regis :', num_regis)

            print('req :', req)


            cModel.setName(name)
            cModel.setCourseID(course_id)
            cModel.setDescription(description)
            cModel.setImage(image)

            cModel.setCdate(cdate)
            cModel.setAdate(adate)
            cModel.setWdate(wdate)
            cModel.setQualification_type(qtype)
            cModel.setContact(contact)

            cModel.setTaType(ta_type)
            cModel.setAnType(an_type)
            cModel.setYear(year)
            cModel.setEnrollNum(enroll_num)
            cModel.setNumRegis(num_regis)


            cModel.setCourseToDB()

            

            print('===================')
            print()

            #* render same page with @app.get() addcourse()
            #! แก้ให้ไตเติ้ลด้วย
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )

        #! continue
        # @self.app.post("/test/editcourse")
        @self.app.post("/editcourse", response_class=HTMLResponse)
        async def editcourse_submit(request : Request,
                                    name:str=Form(...),
                                    course_id:str=Form(...),
                                    description:str=Form(...),
                                    image:str=Form(...),
                                    req:list[str] = Form(...),
                                    cdate:date=Form(...),
                                    adate:date=Form(...),
                                    wdate:datetime=Form(...),
                                    qtype:int=Form(...),
                                    contact:str=Form(...),
                                    ta_type:str=Form(...),
                                    an_type:str=Form(...),
                                    year:str=Form(...),
                                    enroll_num:str=Form(...),
                                    num_regis:str=Form(...)
                                    ):

            print()
            print('========= CourseController.py - @app.post("/editcourse") ==========')
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

            print()
            print('ta_type :', ta_type)
            print('an_type :', an_type)
            print('year :', year)
            print('enroll_num :', enroll_num)
            print('num_regis :', num_regis)

            print('req :', req)

            cModel.setName(name)
            cModel.setCourseID(course_id)
            cModel.setDescription(description)
            cModel.setImage(image)

            cModel.setCdate(cdate)
            cModel.setAdate(adate)
            cModel.setWdate(wdate)
            cModel.setQualification_type(qtype)
            cModel.setContact(contact)

            cModel.setTaType(ta_type)
            cModel.setAnType(an_type)
            cModel.setYear(year)
            cModel.setEnrollNum(enroll_num)
            cModel.setNumRegis(num_regis)

            #! ขา editcourse มีปัญหาเรื่อง sql error ต้องดักเคส primary key วิชาเคยเพิ่มแล้ว
            
            print('----- call CourseModel.py -----')
            cModel.setCourseToDB()
            print('----- ----- ----- ----- -----')
            

            print('===================')
            print()
        
            return self.template.TemplateResponse(
                name="editcourse.html",
                context={"request" : request}
            )

    
    ################## & ##################
        # @self.app.get('/editcourse/{course_id}', response_class=HTMLResponse)
        @self.app.get('/editcourse/{course_history_id}', response_class=HTMLResponse)
        async def editcourse(request : Request, course_history_id):
            print(f"CourseController.py - Received course_history_id: {course_history_id}")
            
            cModel.getDataFromDB(int(course_history_id))

            name = cModel.getName()
            course_id = cModel.getCourseID()
            description = cModel.getDescription()
            image = cModel.getImage()

            cdate = cModel.getCdate()
            adate = cModel.getAdate()
            wdate = cModel.getWdate()
            qualification_type = cModel.getQualification_type()
            contact = cModel.getContact()

            ta_type = cModel.getTaType()
            an_type = cModel.getAnType()
            year = cModel.getYear()
            enroll_num = cModel.getEnrollNum()
            num_regis = cModel.getNumRegis()


            return self.template.TemplateResponse(
                name="editcourse.html",
                # context={"request" : request,
                #          "course_id" : course_id}
                context={"request" : request,
                         "name": name,
                         "course_id":course_id,
                         "description":description,
                         "image":image,
                         "cdate":cdate,
                         "adate":adate,
                         "wdate":wdate,
                        
                        "qtype" :qualification_type,
                        "contact" : contact,
                        "ta_type": ta_type,
                        "an_type": an_type,
                        "year": year,
                        "enroll_num": enroll_num,
                        "num_regis": num_regis,
                        }
            )
