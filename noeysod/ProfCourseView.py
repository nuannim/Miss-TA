from Database import *

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# import uvicorn

class ProfCourseView:
    def __init__(self,
                 db:MySQLDatabase, 
                 app:FastAPI, 
                 template:Jinja2Templates,
                 prof_id):

        # self.db = MySQLDatabase()
        # self.app = FastAPI()
        # self.template = Jinja2Templates(directory='page')

        self.db = db

        self.app = app
        self.app.mount("/static", StaticFiles(directory='static'), name="static")
        self.template = template

        self.prof_id = prof_id

        self.view(self.prof_id)


    def view(self, prof_id):
    ##& app.get()
        #^ admin_subject()
        # @self.app.get('/test', response_class=HTMLResponse)
        @self.app.get('/', response_class=HTMLResponse)
        async def admin_subject(request: Request):
        ##* controller
            self.db.connect()
            query_course_name = ('SELECT c.name '
                                'FROM course AS c '
                                'JOIN prof_course AS pc ON c.course_id = pc.course_id '
                                'WHERE pc.prof_id = %d;') %(prof_id)
            message = self.db.fetch_data(query_course_name)
            message2 = [i['name'] for i in message]
            print(message2)
            # message2 = ['test00', 'test']
        ##*

            return self.template.TemplateResponse(
                name="admin_subject.html",
                context={"request": request, "allProfCourses": message2}
            )
        
        # @self.app.get('/test/addcourse', response_class=HTMLResponse)
        @self.app.get('/addcourse', response_class=HTMLResponse)
        async def addcourse(request : Request):
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )
        
        # @self.app.get('/test/editcourse', response_class=HTMLResponse)
        @self.app.get('/editcourse', response_class=HTMLResponse)
        async def editcourse(request : Request):
            return self.template.TemplateResponse(
                name="editcourse.html",
                context={"request" : request}
            )
    ##&

    ##& app.post()
        # @self.app.post("/test/addcourse", response_class=HTMLResponse)
        @self.app.post("/addcourse", response_class=HTMLResponse)
        async def addcourse_submit(request : Request,
                                name:str=Form(...),
                                course_id:str=Form(...),
                                image:str=Form(...),
                                
                                contact:str=Form(...),
                                
                                    ):
            print(name)
            print(course_id)
            # print(desc)
            print(image)
            # print(req)

            # print(qtype)
            print(contact)

            #* render same page with @app.get() addcourse()
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )

        # @self.app.post("/test/editcourse")
        @self.app.post("/editcourse")
        async def editcourse_submit():
            pass
    ##&





##############################################################################
##############################################################################

# ###! โอ้ยน้องคะ view เอาไว้ใส่การ display เท่านั้นค่ะ ใส่ attribute ไม่ได้ เดี๋นยมาแก้อย่างหนัด
# class ProfCourseView:

# #! จากที่ไปอ่านเรื่อง MVC pattern มา พวกนี้ต้องอยู่ใน controller เท่านั้นจ้ะ
# #! เวลารับค่า controller จะเป็นตัวรับค่า คลาส view ใช้สำหรับแสดงหน้าเท่านั้นเลย
    
#     # def __init__(self, 
#     #             cName = None, 
#     #             cID = None, 
#     #             desc = None, 
#     #             image = None, 
#     #             req = None, 
#     #             req_to_fill = None, 
#     #             adate = None, wdate = None, cdate = None, 
#     #             qtype = None, 
#     #             contact = None):

#     #     self.cName = cName
#     #     self.cID = cID
#     #     self.desc = desc
#     #     self.image = image
#     #     self.req = req
#     #     self.req_to_fill = req_to_fill
#     #     self.adate = adate
#     #     self.wdate = wdate
#     #     self.cdate = cdate
#     #     self.qtype = qtype
#     #     self.contact = contact
#     #     pass

#     def displayMainCourse(self, cName, cID, desc, image, req, reqToFill, adate, wdate, cdate, qtype, contact):
#         #* call fastapi to display these parameter
#         print("::::: ProfCourseView :: debug :::::")
#         print("cname : " + cName)
#         pass

#     # def addCourse():
#     #     pass

#     # def editCourse():
#     #     pass


#     # def getInfoFromDisplay():
#     #     pass

#     # def setInfoToDisplay():
#     #     pass

#     # ตอนเชื่อม ยัดค่าใส่ตาม attribute นี้เลย
#     # def getInfoFromCourseAddEdit(self, 
#     #                          cName, 
#     #                          cID, 
#     #                          desc, 
#     #                          image, 
#     #                          req, 
#     #                          reqToFill, 
#     #                          adate, 
#     #                          wdate, 
#     #                          cdate,
#     #                          qtype,
#     #                          contact):
        
#     #     pass


# ############################################################### !

#     def __init__(self) -> None:
#         pass

