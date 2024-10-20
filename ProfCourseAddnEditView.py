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
        @self.app.get('/addcourse', response_class=HTMLResponse)
        async def addcourse(request : Request):
            return self.template.TemplateResponse(
                name="addcourse.html",
                context={"request" : request}
            )
    ################## & ##################


    ################## & app.post() ##################
        #! ย้าย post ไปไว้ CourseController.py
    ################## & ##################
