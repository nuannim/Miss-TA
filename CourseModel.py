class CourseModel:
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
        self.requirement = requirement # array requirement ที่ add เพิ่มได้ในหน้าวิชา
        self.req_to_fill = req_to_fill # จำเป็นต้องกรอก 0 = no / 1 = yes

#^ getter

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
    def getRequirement(self):
        return self.requirement

    def getReqToFill(self):
        return self.req_to_fill

#^ setter

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
    def setRequirement(self, requirement):
        self.requirement = requirement
    
    def getReqToFill(self, req_to_fill):
        self.req_to_fill = req_to_fill

