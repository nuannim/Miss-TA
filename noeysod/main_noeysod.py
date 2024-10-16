'''run by put 'fastapi dev main_noeysod.py' in terminal'''

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn



#! เดี๋ยวตอนสุดท้ายต้องย้ายพวก @app.get ไปไว้ที่ view ด้วย
###^ update 1ุ6/10/67 ###
    #^ มี app.post() แล้ว แต่มีปัญหาเรื่อง datatype ของ date

app = FastAPI()

# app.mount("/static", StaticFiles(directory='noeysod/static'), name="static")
app.mount("/static", StaticFiles(directory='static'), name="static") #! เดี๋ยวแก้ตาม copilot

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

#################* view

#^ app.get()
@app.get('/', response_class=HTMLResponse)
async def admin_subject(request: Request):
    message2 = [i['name'] for i in message]
    print(message2)
    return template.TemplateResponse(
        name="admin_subject.html",
        context={"request": request, "allProfCourses": message2}
    )

@app.get('/addcourse', response_class=HTMLResponse)
async def addcourse(request : Request):
    return template.TemplateResponse(
        name="addcourse.html",
        context={"request" : request}
    )

@app.get('/editcourse', response_class=HTMLResponse)
async def editcourse(request : Request):
    return template.TemplateResponse(
        name="editcourse.html",
        context={"request" : request}
    )

# @app.get('/')

#^ app.post()
@app.post("/addcourse", response_class=HTMLResponse)
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
    return template.TemplateResponse(
        name="addcourse.html",
        context={"request" : request}
    )

#! continue
@app.post("/editcourse")
async def editcourse_submit():
    pass



if __name__ == "__main_noeysod__":
    uvicorn.run("main_noeysod:app")
