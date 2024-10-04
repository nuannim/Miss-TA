class CourseModel:
    def __init__(self, course_id="", name="", year=0, announce_list_status=False, waiting_list_status=False, description="",image="", adate=None, wdate=None, qualification_type="", contact="", registered_stu_no=0, max_ta=0, num_of_ta=0, num_of_stu_enroll=0):
        self._course_id = course_id
        self._name = name
        self._year = year
        self._announce_list_status = announce_list_status
        self._waiting_list_status = waiting_list_status
        self._description = description
        self._image = image
        self._adate = adate
        self._wdate = wdate
        self._qualification_type = qualification_type
        self._contact = contact
        self._registered_stu_no = registered_stu_no
        self._max_ta = max_ta
        self._num_of_ta = num_of_ta
        self._num_of_stu_enroll = num_of_stu_enroll

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