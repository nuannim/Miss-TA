'''run by put 'fastapi dev main_noeysod.py' in terminal'''

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn



###^ update 1ุ6/10/67 ###
    #^ มี app.post() แล้ว แต่มีปัญหาเรื่อง datatype ของ date


#################* view (มีต่อ)
app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name="static")

template = Jinja2Templates(directory='page')


#################* ลองสร้าง object ดึงวิชาต่าง ๆ (controller)
from ProfessorModel import ProfessorModel
from CourseModel import CourseModel

from Database import *
db = MySQLDatabase()

prof_id = 2
chotipat = ProfessorModel()
chotipatCourse = CourseModel()

chotipat.getDataFromDB(prof_id)
# chotipatCourse.getDataFromDB(prof_id)
#! มันต้องมีไหมวะ
# chotipatCourse.setCourseToDB()

#################* call view class
from ProfCourseView import ProfCourseView
from ProfCourseAddnEditView import ProfCourseAddnEditView

view = ProfCourseView(db, app, template, prof_id, chotipat.getProfCourse())
viewAddEdit = ProfCourseAddnEditView(db, app, template, prof_id)

#################* call controller class
from CourseController import CourseController

controller = CourseController(db, app, template, 
                              chotipat, chotipatCourse, view, viewAddEdit)


if __name__ == "__main_noeysod__":
    uvicorn.run("main_noeysod:app")
