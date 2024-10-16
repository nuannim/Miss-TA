from Database import *

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
                 qualification_type="", 
                 contact="", 
                 registered_stu_no=0, 
                 max_ta=0, 
                 num_of_ta=0, 
                 num_of_stu_enroll=0,
                 requirement=[],
                 req_to_fill=0):

        self._course_id = course_id # รหัสวิชา
        self._name = name # ชื่อวิชา
        self._year = year # ปีที่เรียนวิชานี้
        self._announce_list_status = announce_list_status
        self._waiting_list_status = waiting_list_status
        self._description = description # คำอธิบายวิชา
        self._image = image # รูปปกวิชา
        self._adate = adate # announce_date วันประกาศผล
        self._wdate = wdate # waiver_date วันสละสิทธิ์

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
        self._requirement = requirement # array requirement ที่ add เพิ่มได้ในหน้าวิชา
        self._req_to_fill = req_to_fill # จำเป็นต้องกรอก 0 = no / 1 = yes

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

    def getReqToFill(self):
        return self._req_to_fill


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

    # requirement + required to fill?
    #! เดี๋ยวเอาออกด้วย ไม่น่าจะได้ใช้
    #! รอเชื่อมก่อนค่อยว่ากัน

    def setRequirement(self, requirement):
        self._requirement = requirement
    
    def setReqToFill(self, req_to_fill):
        self._req_to_fill = req_to_fill

#^ db getter : getDataFromDB
    def getDataFromDB(self, which_course_id):
        '''get(import) all data from database then set it into CourseModel.py attribute'''
        # เป็น method สำหรับดึงจาก database โดยตรง
        # เดี๋ยวมาเขียน

        self.db.connect()
        
        #* query_course
        query_course = 'select * from course where course_id = %d' %which_course_id
        message = self.db.fetch_data(query_course)

        print(message)

        self.setCourseID(message[0]['course_id'])
        self.setName(message[0]['name'])
        self.setYear(message[0]['YEAR'])
        self.setAnnounceL_Status(message[0]['description'])
        self.setWaitingL_Status(message[0]['image'])
        self.setDescription(message[0]['adate'])
        self.setImage(message[0]['wdate'])
        self.setAdate(message[0]['cdate'])
        self.setWdate(message[0]['qtype'])
        self.setCdate(message[0]['contact'])
        self.setQualification_type(message[0]['qtype'])
        self.setContact(message[0]['contact'])

        #* query history
        # query_history = 'select * from history'
        query_history = 'select * from history, enroll\
                        where history.enroll_id = enroll.enroll_id\
                        and course_id = %d' %which_course_id
        message_history = self.db.fetch_data(query_history)
        # print('message_history :', message_history)
        # print('ta registered stu number :', len(message_history))
        self.setRegisteredStuNo(len(message_history))
        # self.setMaxTA(message[0]['']) #! คำนวณยังไง
        # self.setNumOfTA(message[0]['']) #! อันนี้อะไร

        #* query_enroll
        query_enroll = 'select * from enroll where course_id = %d' %which_course_id
        message_enroll = self.db.fetch_data(query_enroll)

        # print(message_enroll)

        # print(len(message_enroll))
        self.setNumOfStuEnroll(len(message_enroll))

        #! เดี๋ยวเอาออกด้วย ไม่น่าจะได้ใช้
        # self.setRequirement(message[0][''])
        # self.setReqToFill(message[0][''])

        self.db.close()


#^ db setter : setDataToDB
    def setDataToDB(self):
        """ยังไม่ได้ทำ"""
        # เป็น method สำหรับส่งข้อมูลไป database โดยตรง
        # เดี๋ยวมาเขียน
        self.db.connect()

        #* insert_course
        add_course_test = 'insert into course( \
            course_id, name, year, description, image, \
            adate, wdate, cdate, qtype, contact)\
                values (%s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s)'

        data = (self.getCourseID(), self.getName(), self.getYear(), self.getDescription(), self.getImage(),
                self.getAdate(), self.getWdate(), self.getCdate(), self.getQualification_type(), self.getContact())

        # add_course_test = ('insert into course(name, course_id, description)'
        #                    'values (%s, %s, %s)')
        
        # data = (self.getName(), self.getCourseID(), self.getDescription())
        # # data = ('test', 848484, 'test ahhhhh')

        self.db.insert_data(add_course_test, data)

        #* insert_history




        #* insert_enroll
