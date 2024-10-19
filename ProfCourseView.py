from Database import *

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# import uvicorn

#* เดี่ยวจัดระเบียบใหม่ด้วย พวก pCourseName ...
class ProfCourseView:
    def __init__(self,
                 db:MySQLDatabase, 
                 app:FastAPI, 
                 template:Jinja2Templates,
                 prof_id,
                 pCourseName):

        # self.db = MySQLDatabase()
        # self.app = FastAPI()
        # self.template = Jinja2Templates(directory='page')

        self.db = db

        self.app = app
        self.app.mount("/static", StaticFiles(directory='static'), name="static")
        self.template = template

        self.prof_id = prof_id
        self.prof_course_name_list = pCourseName

        self.view(self.prof_id)


    def view(self, prof_id):

    ################## & app.get() ##################
        #^ admin_subject()
        # @self.app.get('/test', response_class=HTMLResponse)
        @self.app.get('/', response_class=HTMLResponse)
        async def admin_subject(request: Request):
        ##* 
            message = self.prof_course_name_list
            message2 = [i for i in message]
            print()
            print('====================')
            print('ProfCourseView.py :', message2)
            print('====================')
            print()
        ##*

            return self.template.TemplateResponse(
                name="admin_homepage.html",
                context={"request": request, "allProfCourses": message2}
            )
    ################## & ##################
