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
        
        # @self.app.get('/test/editcourse', response_class=HTMLResponse)
        @self.app.get('/editcourse', response_class=HTMLResponse)
        async def editcourse(request : Request):
            return self.template.TemplateResponse(
                name="editcourse.html",
                context={"request" : request}
            )
    ################## & ##################

    ################## & app.post() ##################
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

        #! continue
        # @self.app.post("/test/editcourse")
        @self.app.post("/editcourse")
        async def editcourse_submit():
            pass


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