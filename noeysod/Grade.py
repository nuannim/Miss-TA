class Grade:
    def __init__(self,course_id = "", grade=""):
        self.course_id = course_id
        self.grade = grade
    
    def setcourse_id(self,course_id):
        self.course_id = course_id
    
    def setgrade(self,grade):
        self.grade = grade
        
    def getcourse_id(self):
        return self.course_id
    
    def getgrade(self):
        return self.grade
