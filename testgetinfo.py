from QualificationController import *

def getNumOfCouse():
        x = 10 #query จำนวนวิชาที่เปิดรับสมัคร
        return x

def main():
    num = getNumOfCouse()
    g = getInfoFromDB(66070276,num)
    for i in range(num):
        g.setCourseModel(i)
        gms = g.Course[i].getNumOfTA()
        print(gms)

 
main()