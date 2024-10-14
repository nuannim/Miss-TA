from QualificationController import *
from generalController import *
def getNumOfCouse():
       g = generalController()
       return g.getNumOfCourse()

def main():
    num = getNumOfCouse()
    print(num)
    g = getInfoFromDB(66070276,int(num))
    for i in range(num):
        g.setCourseModel(i)
        gms = g.Course[i].getName()
        print(gms)
 
main()