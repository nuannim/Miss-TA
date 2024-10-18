from Database import *

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# import uvicorn

class ProfCourseAddnEditView:
    def __init__(self,
                 db:MySQLDatabase, 
                 app:FastAPI, 
                 template:Jinja2Templates, 
                 prof_id):

        self.db = db

        self.app = app
        self.app.mount("/static", StaticFiles(directory='static'), name="static")
        self.template = template

        self.prof_id = prof_id

        self.viewAddEdit(self.prof_id)


    def viewAddEdit(self, prof_id):
    ################## & app.get() ##################
        # @self.app.get('/test/addcourse', response_class=HTMLResponse)
        @self.app.get('/addcourse', response_class=HTMLResponse)
        async def addcourse(request : Request):
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )
        
        # # @self.app.get('/test/editcourse', response_class=HTMLResponse)
        # @self.app.get('/editcourse/{course_id}', response_class=HTMLResponse)
        # async def editcourse(request : Request, course_id):
        #     print(f"Received course_id: {course_id}")

        #     return self.template.TemplateResponse(
        #         name="editcourse.html",
        #         # context={"request" : request,
        #         #          "course_id" : course_id}
        #         context={"request" : request}
        #     )
    ################## & ##################


    ################## & app.post() ##################
        #! ย้าย post ไปไว้ CourseController.py
    ################## & ##################



###################################
###################################

# class ProfCourseAddnEditView:
#     def __init__(self) -> None:
#         pass

#     def displayPage():
#         pass

#     def done():
#         pass

#     def getInfoFromDisplay(self):
#         pass

#     def setInfoFromDisplay(self):
#         pass
