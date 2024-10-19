from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from StudentCourseController import *
from Database import *
from Requirement import *
from CourseModel import *
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# กำหนดตำแหน่งของ Jinja2 template
templates = Jinja2Templates(directory="page")


import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    scc = StudentCourseController(66070998)

    # รัน setStudentInfo() ใน thread
    await asyncio.to_thread(scc.setStudentInfo)
    
    # รัน getCourseForStudent() ใน thread และรับค่าผลลัพธ์
    course = await asyncio.to_thread(scc.getCourseForStudent)

    course_data = []
    coursefdata = []
    for i in course:
        if isinstance(i, CourseModel):  
            name = i.getName()
            descrip = i.getDescription()
            cid = i.getCourseID()
            status = scc.checkstatus(cid)
            tup = {"name": name, "status": status, "description": descrip, "index_id": i, "course_id": cid}
            if status:
                course_data.append(tup)
            else:
                coursefdata.append(tup)

    return templates.TemplateResponse("user_homepage.html", {"request": request, "courses": course_data, "coursef": coursefdata})
    

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