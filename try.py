#! python3
import csv
from tool import *
with open('ALL0008/F0008CH2.CSV','r') as myFile:
    lines=csv.reader(myFile)
    a=[]
    b=[]
    print("start")
    i=0
    for line in lines:
        #a.append(float(line[3]))
        #b.append(float((line[4])[1:10]))
        if i == 11:
            print(line[1])
            a=line[1]
            print('{:.5f}'.format(float(a)))
        i=i+1
    print("OK")
    #print(b[0])

# dogone=NbDog(a,b)
# print(dogone.ffdog())
# dogone.plotdog()
