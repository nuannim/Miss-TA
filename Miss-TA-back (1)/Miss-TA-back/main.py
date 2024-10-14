from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from QualificationController import *
from generalController import *
from Database import *
app = FastAPI()
app.mount("/static", StaticFiles(directory="/Miss-TA-front/static"), name="static")
# กำหนดตำแหน่งของ Jinja2 template
templates = Jinja2Templates(directory="Miss-TA-front\page")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    gen = generalController()
    num = gen.getNumOfCourse()
    info = getInfoFromDB(66070276,num)
    course_data = []
    for i in range(num):
        info.setCourseModel(i)
        name = info.Course[i].getName()
        status = ""
        descrip = info.Course[i].getDescription()
        cid = info.Course[i].getCourseID()
        year = info.Course[i].getYear()
        if gen.checkstatus(66070276,cid,year) == True:
            status = "สมัครได้"
        elif gen.checkstatus(66070276,cid,year) == False:
            status = "สมัครไม่ได้"
        tup = {"name": name, "status": status, "description": descrip, "index_id" : i, "course_id" : cid}
        course_data.append(tup)
    
    return templates.TemplateResponse("user_subject.html", {"request": request, "courses": course_data})

@app.get("/course/{index_id}", response_class=HTMLResponse)
async def course_detail(request: Request, index_id: int, course_id: int):
    print(course_id)
    course_data = []
    req_data = []
    nonreq_data = []
    gen = generalController()
    db = MySQLDatabase()
    name = gen.getnamecourse(index_id)
    des = db.getCourseDes(index_id)
    tup = {"name": name, "description": des}
    course_data.append(tup)
    num = db.getNumOfReq(course_id)
    for i in range(num):

        req_list = db.getreq(course_id)
        if req_list[i]['required_to_fill'] == 0:
            qest_0 = req_list[i]['req_question']
            tup0 = {"qest0" : qest_0}
            nonreq_data.append(tup0)
        elif req_list[i]['required_to_fill'] == 1:
            qest_1 = req_list[i]['req_question']
            tup1 = {"qest" : qest_1}
            req_data.append(tup1)

    return templates.TemplateResponse("course.html", {"request": request, "courses": course_data, "req1": req_data, "req0" : nonreq_data})