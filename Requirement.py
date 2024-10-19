class Requirement:
    def __init__(self,req="",type=""):
        self.req = req
        self.type = type
    
    def setReq(self,req):
        self.req = req
    
    def setType(self,type):
        self.type = type

    def getReq(self):
        return self.req
    
    def getType(self):
        return self.type

