'''run by put 'fastapi dev main_noeysod.py' in terminal'''

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn



#! เดี๋ยวตอนสุดท้ายต้องย้ายพวก @app.get ไปไว้ที่ view ด้วย
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

prof_id = 1
chotipat = ProfessorModel()
chotipatCourse = CourseModel()

chotipat.getDataFromDB(prof_id)
# chotipatCourse.getDataFromDB(prof_id)

db.connect()
query_course_name = ('SELECT c.name '
                     'FROM course AS c '
                     'JOIN prof_course AS pc ON c.course_id = pc.course_id '
                     'WHERE pc.prof_id = %d;') %(prof_id)
message = db.fetch_data(query_course_name)
print('message from query :', message)
db.close()

#################* if view in view file
from ProfCourseView import ProfCourseView

view = ProfCourseView(db, app, template, prof_id)

if __name__ == "__main_noeysod__":
    uvicorn.run("main_noeysod:app")
