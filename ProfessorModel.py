class Professor:
    def __init__(self, first_name="", last_name="", num_of_course=0, course=None, teacher_id=""):
        self._first_name = first_name
        self._last_name = last_name
        self._num_of_course = num_of_course
        self._course = course if course is not None else []
        self._teacher_id = teacher_id

#^ getter

    def getFirstName(self):
        return self._first_name

    def getLastName(self):
        return self._last_name

    def getNumOfCourse(self):
        return self._num_of_course

    def getCourse(self):
        return self._course

    def getTeacherId(self):
        return self._teacher_id

#^ setter

    def setFirstName(self, first_name):
        self._first_name = first_name

    def setLastName(self, last_name):
        self._last_name = last_name

    def setNumOfCourse(self, num_of_course):
        self._num_of_course = num_of_course

    def setCourse(self, course):
        if isinstance(course, list):
            self._course = course
        else:
            self._course = [course]

    def setTeacherId(self, teacher_id):
        self._teacher_id = teacher_id