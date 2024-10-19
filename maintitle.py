from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from StudentCourseController import *
from Database import *
from Requirement import *
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# กำหนดตำแหน่งของ Jinja2 template
templates = Jinja2Templates(directory="page")

# scc = StudentCourseController(66070998)
# course = scc.getCourseForStudent()

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    
    # print("---------------------")
    # # print(course)
    # print("---------------------")
    # # course_data = []
    # for i in course:
    #     if isinstance(i, CourseModel):
    #         name = i.getName()
    #         status = i.getQualification_type()
    #         descrip = i.getDescription()
    #         cid = i.getCourseID()
    #         tup = {"name": name, "status": status, "description": descrip, "index_id" : i, "course_id" : cid}
    #         course_data.append(tup)
    
    return templates.TemplateResponse("user_homepage.html", {"request": request})

@app.get("/course/{course_id}", response_class=HTMLResponse)
async def course_detail(request: Request,course_id: int):
    # print("Courseforreq")
    # print(course_id)
    # print("Courseforreq")
    # print(course_id)
    # course_data = []
    # req_data = []
    # nonreq_data = []
    # req_list = [Requirement]
    # for i in course:
    #     if isinstance(i, CourseModel): 
    #         if i.getCourseID() == course_id:
    #             name = i.getName()
    #             des = i.getDescription()
    #             tup = {"name": name, "description": des}
    #             course_data.append(tup)
    #             req_list = i.getRequirement()  # เรียกเมธอด getRequirement() เพื่อนำข้อมูล Requirement

    #             for j in req_list:
    #                 if isinstance(j, Requirement): 
    #                     if j.getType() == 0:  # ตรวจสอบว่า required_to_fill == 0
    #                         qest_0 = j.getReq()
    #                         tup0 = {"qest0": qest_0}
    #                         nonreq_data.append(tup0)
    #                     elif j.getType() == 1:  # ตรวจสอบว่า required_to_fill == 1
    #                         qest_1 = j.getReq()
    #                         tup1 = {"qest": qest_1}
    #                         req_data.append(tup1)


    return templates.TemplateResponse("course.html", {"request": request})