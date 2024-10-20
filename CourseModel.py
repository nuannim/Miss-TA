from Database import *
from Requirement import *

from datetime import date

class CourseModel:
    '''ดูแลตาราง course / enroll / prof_req / history'''
    def __init__(self, 
                 course_id="", 
                 name="", 
                 year=0, 
                 announce_list_status=False, 
                 waiting_list_status=False, 
                 description="",
                 image="", 
                 adate=None, 
                 wdate=None, 
                 cdate=None,
                 qualification_type=False, 
                 contact="", 
                 registered_stu_no=0, 
                 max_ta=0, 
                 num_of_ta=0, 
                 num_of_stu_enroll=0,
                 requirement='',

                 course_history_id=0,
                 
                 ta_type='',
                 an_type='',
                 enroll_num='',
                 num_regis=''):

        self._course_id = course_id # รหัสวิชา
        self._name = name # ชื่อวิชา
        self._year = year # ปีที่เรียนวิชานี้
        self._announce_list_status = announce_list_status
        self._waiting_list_status = waiting_list_status
        self._description = description # คำอธิบายวิชา
        self._image = image # รูปปกวิชา
        self._adate = adate # announce_date วันประกาศผล
        self._wdate = wdate # waiver_date วันสละสิทธิ์/วันยืนยันสิทธิ์

        # วันปิดรับสมัคร ?
        self._cdate = cdate # closed_date วันปืดรับสมัคร

        self._qualification_type = qualification_type # วิธีการคัดเลือก (อจ/ระบบ)
        self._contact = contact # เบอร์โทรศัพท์
        self._registered_stu_no = registered_stu_no # นศทั้งหมดที่สมัครเป็น TA
        self._max_ta = max_ta # TA ที่มากที่สุดในวิชา
        self._num_of_ta = num_of_ta # จำนวน TA
        self._num_of_stu_enroll = num_of_stu_enroll # นศที่ลงทะเบียนเรียนวิชา

        # requirement + required to fill?
        #! เดี๋ยวเอาออกด้วย ไม่น่าจะได้ใช้
        #! รอเชื่อมก่อนค่อยว่ากัน
        # self._requirement = [Requirement] # array requirement ที่ add เพิ่มได้ในหน้าวิชา
        self._requirement = requirement
        self._course_history_id=course_history_id

        self._ta_type = ta_type
        self._an_type = an_type
        self._enroll_num = enroll_num
        self._num_regis = num_regis


        self.db = MySQLDatabase()


#^ attribute : getter

    def getCourseID(self):
        return self._course_id

    def getName(self):
        return self._name

    def getYear(self):
        return self._year

    def getAnnounceL_Status(self):
        return self._announce_list_status

    def getWaitingL_Status(self):
        return self._waiting_list_status

    def getDescription(self):
        return self._description

    def getImage(self):
        return self._image

    def getAdate(self):
        return self._adate

    def getWdate(self):
        return self._wdate

    # cdate
    def getCdate(self):
        return self._cdate

    def getQualification_type(self):
        return self._qualification_type

    def getContact(self):
        return self._contact

    def getRegisteredStuNo(self):
        return self._registered_stu_no

    def getMaxTA(self):
        return self._max_ta

    def getNumOfTA(self):
        return self._num_of_ta

    def getNumOfStuEnroll(self):
        return self._num_of_stu_enroll
    
    # requirement + required to fill?
    #! เดี๋ยวเอาออกด้วย ไม่น่าจะได้ใช้
    #! รอเชื่อมก่อนค่อยว่ากัน

    def getRequirement(self):
        return self._requirement

    def getCourseHistoryID(self):
        return self._course_history_id

#* new
    def getTaType(self):
        return self._ta_type

    def getAnType(self):
        return self._an_type

    def getEnrollNum(self):
        return self._enroll_num
    
    def getNumRegis(self):
        return self._num_regis
    

#^ attribute : setter

    def setCourseID(self, course_id):
        self._course_id = course_id

    def setName(self, name):
        self._name = name

    def setYear(self, year):
        self._year = year

    def setAnnounceL_Status(self, status):
        self._announce_list_status = status

    def setWaitingL_Status(self, status):
        self._waiting_list_status = status

    def setDescription(self, description):
        self._description = description

    def setImage(self, image):
        self._image = image

    def setAdate(self, adate):
        self._adate = adate

    def setWdate(self, wdate):
        self._wdate = wdate

    # cdate
    def setCdate(self, cdate):
        self._cdate = cdate

    def setQualification_type(self, qualification_type):
        self._qualification_type = qualification_type

    def setContact(self, contact):
        self._contact = contact

    def setRegisteredStuNo(self, registered_stu_no):
        self._registered_stu_no = registered_stu_no

    def setMaxTA(self, max_ta):
        self._max_ta = max_ta

    def setNumOfTA(self, num_of_ta):
        self._num_of_ta = num_of_ta

    def setNumOfStuEnroll(self, num_of_stu_enroll):
        self._num_of_stu_enroll = num_of_stu_enroll

    # def add_requirement(self, requirement):
    #     if isinstance(requirement, Requirement):
    #         self._requirement.append(requirement)
    #     else:
    #         raise TypeError("ต้องเป็น object ของคลาส Requirement เท่านั้น")

    def setRequirement(self, requirement):
        self._requirement = requirement

    def setCourseHistoryID(self, course_history_id):
        self._course_history_id = course_history_id

#* new
    def setTaType(self, ta_type):
        self._ta_type = ta_type

    def setAnType(self, an_type):
        self._an_type = an_type

    def setEnrollNum(self, enroll_num):
        self._enroll_num = enroll_num

    def setNumRegis(self, num_regis):
        self._num_regis = num_regis




#^ db getter : getDataFromDB
    def getDataFromDB(self, which_course_history_id):
        '''get(import) all data from database then set it into CourseModel.py attribute'''
        # เป็น method สำหรับดึงจาก database โดยตรง

        self.db.connect()
        
        # query_course
        # query_course = 'select * from course where course_id = %d' %which_course_id
        # message = self.db.fetch_data(query_course)

        # print(message)

        # self.setCourseID(message[0]['course_id'])
        # self.setName(message[0]['name'])
        # self.setYear(message[0]['YEAR'])
        # self.setDescription(message[0]['description'])
        # self.setImage(message[0]['image'])
        # self.setAdate(message[0]['adate'])
        # self.setWdate(message[0]['wdate'])
        # self.setCdate(message[0]['cdate'])
        # self.setQualification_type(message[0]['qtype'])
        # self.setContact(message[0]['contact'])


        # query history
        # query_history = 'select * from history, enroll\
        #                 where history.enroll_id = enroll.enroll_id\
        #                 and course_id = %d' %which_course_id
        # message_history = self.db.fetch_data(query_history)

        # self.setRegisteredStuNo(len(message_history))
        # # self.setMaxTA(message[0]['']) #! คำนวณยังไง
        # # self.setNumOfTA(message[0]['']) #! อันนี้อะไร

        # query_enroll
        # query_enroll = 'select * from enroll where course_id = %d' %which_course_id
        # message_enroll = self.db.fetch_data(query_enroll)

        # self.setNumOfStuEnroll(len(message_enroll))

        #! เดี๋ยวเอาออกด้วย ไม่น่าจะได้ใช้
        # ไตเติ้ลเพิ่งเขียน class ใหม่ ลองเอาไปใช้ได้
        # self.setRequirement(message[0][''])
        # self.setReqToFill(message[0][''])

        ############* new insert ############

        #* query_course_equijoin_course_history
        query_course_equijoin_course_history = ('SELECT * FROM course ' 
                                                'JOIN course_history ' 
                                                'ON course.course_id = course_history.course_id '
                                                'WHERE course_history_id = %s' %which_course_history_id)
        fetch_courseNcoursehistory = self.db.fetch_data(query_course_equijoin_course_history)

        print()
        print('query_course_equijoin_course_history :: CourseModel.py :', fetch_courseNcoursehistory)
        print()

        self.setCourseID(fetch_courseNcoursehistory[0]['course_id'])
        self.setName(fetch_courseNcoursehistory[0]['name'])
        self.setYear(fetch_courseNcoursehistory[0]['YEAR'])
        self.setDescription(fetch_courseNcoursehistory[0]['description'])
        self.setImage(fetch_courseNcoursehistory[0]['image'])
        self.setAdate(fetch_courseNcoursehistory[0]['adate'])
        self.setWdate(fetch_courseNcoursehistory[0]['wdate'])
        self.setCdate(fetch_courseNcoursehistory[0]['cdate'])
        self.setQualification_type(fetch_courseNcoursehistory[0]['qtype'])
        self.setContact(fetch_courseNcoursehistory[0]['contact'])

        self.setCourseHistoryID(fetch_courseNcoursehistory[0]['course_history_id'])
        self.setTaType(fetch_courseNcoursehistory[0]['ta_type'])
        self.setAnType(fetch_courseNcoursehistory[0]['an_type'])
        self.setNumRegis(fetch_courseNcoursehistory[0]['num_regis'])
        self.setEnrollNum(fetch_courseNcoursehistory[0]['enroll_num'])

        self.setRequirement(fetch_courseNcoursehistory[0]['req'])

        self.db.close()


#^ db setter : setCourseToDB() / setHistoryToDB()
    def setCourseToDB(self):
        """มีแค่ insert_course อย่างเดียว"""
        # เป็น method สำหรับส่งข้อมูลไป database โดยตรง
        # เดี๋ยวมาเขียน
        self.db.connect()

        # insert_course
        # add_course_test = 'insert into course( \
        #     course_id, name, year, description, image, \
        #     adate, wdate, cdate, qtype, contact)\
        #         values (%s, %s, %s, %s, %s,\
        #             %s, %s, %s, %s, %s)'

        # data = (self.getCourseID(), self.getName(), self.getYear(), self.getDescription(), self.getImage(),
        #         self.getAdate(), self.getWdate(), self.getCdate(), self.getQualification_type(), self.getContact())

        # self.db.insert_data(add_course_test, data)

        ############* new insert ############

        print('++++++++++++ CourseModel.py - setCourseToDB() ++++++++++++')
        #* insert_course (new)
        try:
            add_course = ('insert into course(course_id, name, year, enroll_num) values (%s, %s, %s, %s)')
            data = (self.getCourseID(), self.getName(), self.getYear(), self.getEnrollNum())
            self.db.insert_data(add_course, data)

            print('insert_course successfully')
        except Exception as e:
            print(f"Error inserting course: {e}")

        #* insert_course_history (new)
        # Always attempt to insert course history
        add_course_history = ('insert into course_history(course_id, description, adate, wdate, cdate, qtype, contact, image, ta_type, an_type, num_regis, req) '
                              'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)')
        data_history = (self.getCourseID(), self.getDescription(), self.getAdate(), self.getWdate(), self.getCdate(), 
                        self.getQualification_type(), self.getContact(), self.getImage(), self.getTaType(), self.getAnType(), self.getNumRegis(), self.getRequirement())
        self.db.insert_data(add_course_history, data_history)

        print('insert_course_history successfully')

        print('++++++++++++ ++++++++++++')


        #* insert_history ==> ไม่ใช่ตรงนี้ละ เพิ่งฉุกคิดได้ว่า history จะเกิดขึ้นเมื่ออจเลือกนศแล้วกด submit
        #*                      sooo ต้องแยก method
        #*                ==> อีกเรื่องคือ usecase ที่ทำไม่มีเรื่องนี้ = ไม่ต้องเขียนก็ได้

        #* insert_enroll ==> คือจริง ๆ เราไม่ได้ใส่ลิสคน enroll ด้วยอันนี้ เราดึงจากคณะเอา

        self.db.close()

    def setHistoryToDB(self):
        '''set history everytime we make transaction'''
        pass

    def setProfCourseToDB(self, which_prof_id):
        # add_prof_course =
        pass

    def updateCourseToDB(self, which_course_history_id):
        pass