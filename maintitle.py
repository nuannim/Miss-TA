from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from StudentCourseController import StudentCourseController
from CourseModel import CourseModel
import asyncio

class userCourseView:
    def __init__(self,
                 db, 
                 app: FastAPI, 
                 templates: Jinja2Templates):
        self.db = db
        self.app = app
        self.templates = templates
        
        # ตั้งค่า static files
        app.mount("/static", StaticFiles(directory='static'), name="static")

    def userview(self):
        @self.app.get("/user", response_class=HTMLResponse)
        async def homepage(request: Request):
            scc = StudentCourseController(66070998)

            # เรียกใช้ setStudentInfo() ใน thread
            await asyncio.to_thread(scc.setStudentInfo)
            
            # เรียกใช้ getCourseForStudent() ใน thread และรับค่าผลลัพธ์
            courses = await asyncio.to_thread(scc.getCourseForStudent)

            # แยกข้อมูลหลักสูตรตามสถานะ
            course_data = [
                {
                    "name": i.getName(),
                    "status": scc.checkstatus(i.getCourseID()),
                    "description": i.getDescription(),
                    "index_id": i,
                    "course_id": i.getCourseID(),
                    "coursehistoryid": i.getCourseHistoryID(),
                    "image" : i.getImage()
                }
                for i in courses if isinstance(i, CourseModel)
            ]
            
            # แยกข้อมูลตามสถานะ
            course_passed = [c for c in course_data if c["status"]]
            course_failed = [c for c in course_data if not c["status"]]

            # แสดงผลหน้า user_homepage.html
            return self.templates.TemplateResponse("user_homepage.html", {"request": request, "courses": course_passed, "coursef": course_failed})
    
        @self.app.get("/user/course/{course_id}", response_class=HTMLResponse)
        async def course_detail(request: Request, course_id: int):
            print("Courseforreq")
            print(course_id)
            print("Courseforreq")
            print(course_id)
            course_data = []
            req_data = []
            nonreq_data = []
            req = ""
            course = CourseModel()
            tup2 = {}
            course.getDataFromDB(course_id)
            course.getName()
            course.getDescription()
            course.getRequirement()
            tup = {"description": course.getDescription(), "name": course.getName()}
            if course.getRequirement() != "" or course.getRequirement() != None:
                tup2 = {"req1": course.getRequirement()}
                req_data.append(tup2)
            course_data.append(tup)
            # แสดงผลหน้า course.html
            return self.templates.TemplateResponse("course.html", {"request": request,"courses": course_data, "req": req_data})
