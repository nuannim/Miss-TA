class ProfCourseView:
    def __init__(self, 
                cName = None, 
                cID = None, 
                desc = None, 
                image = None, 
                req = None, 
                req_to_fill = None, 
                adate = None, wdate = None, cdate = None, 
                qtype = None, 
                contact = None):

        self.cName = cName
        self.cID = cID
        self.desc = desc
        self.image = image
        self.req = req
        self.req_to_fill = req_to_fill
        self.adate = adate
        self.wdate = wdate
        self.cdate = cdate
        self.qtype = qtype
        self.contact = contact
        pass

    def displayMainCourse():
        pass

    def addCourse():
        pass

    def editCourse():
        pass

    def getInfoFromDisplay():

        pass

    # def setInfoToDisplay():
    #     pass

    # ตอนเชื่อม ยัดค่าใส่ตาม attribute นี้เลย
    # def getInfoFromCourseAddEdit(self, 
    #                          cName, 
    #                          cID, 
    #                          desc, 
    #                          image, 
    #                          req, 
    #                          reqToFill, 
    #                          adate, 
    #                          wdate, 
    #                          cdate,
    #                          qtype,
    #                          contact):
        
    #     pass

    def getcName(self):
        return self.cName

    def getcID(self):
        return self.cID
    
    def getdesc(self):
        return self.desc
    
    def getimage(self):
        return self.image
    
    def getreq(self):
        return self.req
    
    def getreq_to_fill(self):
        return self.req_to_fill
    
    def getadate(self):
        return self.adate
    
    def getwdate(self):
        return self.wdate
    
    def getcdate(self):
        return self.cdate
    
    def getqtype(self):
        return self.qtype
 
    def getcontact(self):
        return self.contact

