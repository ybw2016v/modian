#! python3
import matplotlib.pyplot as plt
import csv
class NbDog(object):
    """docstring for NbDog"""
    time=[]
    v=[]
    ff=0
    def __init__(self, a,b):
        super(NbDog, self).__init__()
        self.time=a
        self.v=b
    def ffdog(self):
        maxdog=max(self.v)
        mindog=min(self.v)
        self.ff=maxdog-mindog
        return self.ff
        pass
    def plotdog(self):
        plt.figure(figsize=(4,3))
        plt.plot(self.time,self.v,'-')
        plt.legend()
        plt.show()
        pass

class Autodog(object):
    """docstring for Autodog."""
    def __init__(self, DogName):
        self.DogNamel=DogName
        self.Namea=DogName[0]+'/'+DogName[1]+'.CSV'
        self.Nameb=DogName[0]+'/'+DogName[2]+'.CSV'
        pass
    def readdog(self):
        with open(self.Namea,'r') as myFile:
            linesb=csv.reader(myFile)
            i=0
            for dog in linesb:
                if i ==11:
                    self.timedog=dog[1]
                    self.timedog=float(self.timedog)
                i=i+1
            print(self.timedog)
        with open(self.Namea,'r') as myFile:
            lines=csv.reader(myFile)
            self.Adoga=[]
            self.Adogb=[]
            print("start")
            i=0
            #linesb=lines
            # for line in linesb:
            #     if i==11:
            #         self.timedog=line[1]
            #         self.timedog=float(self.timedog)
            #         print(self.timedog)
            #     i=i+1
            for line in lines:
                #print(line)
                self.Adoga.append(float(line[3]))
                self.Adogb.append(float((line[4])[1:10]))
            print("OK")

        with open(self.Nameb,'r') as myFile:
            lines=csv.reader(myFile)
            self.Bdoga=[]
            self.Bdogb=[]
            print("start")
            for line in lines:
                #print(line)
                self.Bdoga.append(float(line[3]))
                self.Bdogb.append(float((line[4])[1:10]))
            print("OK")
        pass
    def fengdog(self):
        self.Aff=max(self.Adogb)-min(self.Adogb)
        self.Bff=max(self.Bdogb)-min(self.Bdogb)
        return [self.Aff,self.Bff]
        pass
    def figdog(self):
        plt.figure(figsize=(4,2))
        plt.plot(self.Adoga,self.Adogb,'-')
        # plt.xlabel('time(s)')
        # plt.ylabel('V(v)')
        plt.legend()
        alu=self.Namea=self.DogNamel[0]+'/'+self.DogNamel[1]+'.jpg'
        plt.savefig(alu)
        plt.figure(figsize=(4,2))
        plt.plot(self.Bdoga,self.Bdogb,'-')
        # plt.xlabel('time(s)')
        # plt.ylabel('V(v)')
        plt.legend()
        blu=self.Nameb=self.DogNamel[0]+'/'+self.DogNamel[2]+'.jpg'
        #plt.show()
        plt.savefig(blu)
        pass
    def pindog(self):
        self.dui1=[]
        self.dui2=[]
        for dog in self.Adoga:
            pig=self.Adogb[self.Adoga.index(dog)]
            self.dui1.append([dog,pig])
            pass
        for dog in self.Bdoga:
            pig=self.Bdogb[self.Bdoga.index(dog)]
            self.dui2.append([dog,pig])
            pass
        dui1=self.dui1
        dui2=self.dui2
        pudog=0
        self.pin1=0
        i=0
        pu=self.Aff*0.05
        for d in range(1,len(dui1)-1200):
            i=i+1
            #print(dui2[i][1])
            if abs(dui1[i][1]+dui1[i+1][1]) < pu and pudog==0:
                #print(dui2[i][1])
                pudog=1
                hitdog=dui1[i][0]
                #print(i)
                i=i+400
            if (abs(dui1[i][1]+dui1[i+1][1]) < pu  and pudog==1):
                pudog=2
                i=i+400
                #print(i)
            if (abs(dui1[i][1]+dui1[i+1][1]) < pu and pudog==2):
                pudog=8
                hitdog=dui1[i][0]-hitdog
                self.pin1=float(float(1)/float(hitdog))
                #print(self.pin2)
                i=i+300
        print(self.pin1)
        pudog=0
        self.pin2=0
        i=0
        pu=self.Bff*0.05
        for d in range(1,len(dui2)-1200):
            i=i+1
            #print(dui2[i][1])
            if abs(dui2[i][1]+dui2[i+1][1]) < pu and pudog==0:
                #print(dui2[i][1])
                pudog=1
                hitdog=dui2[i][0]
                #print(i)
                i=i+400
            if (abs(dui2[i][1]+dui2[i+1][1]) < pu  and pudog==1):
                pudog=2
                i=i+400
                #print(i)
            if (abs(dui2[i][1]+dui2[i+1][1]) < pu and pudog==2):
                pudog=8
                hitdog=dui2[i][0]-hitdog
                self.pin2=float(float(1)/float(hitdog))
                #print(self.pin2)
                i=i+300
        print(self.pin2)
    def wridog(self):
        with open('res.md','a') as myFile:
            pin=str('%d'%(2*int(self.pin2)))
            a='|'+str(pin)+'|'+str('{:.2f}'.format(self.Bff))+'|'+'!['+self.Nameb+']'
            a=a+'('+self.Nameb+')'+'|'+str('{:.2f}'.format(self.Aff))+'|'+'!['+self.Namea+']'
            a=a+'('+self.Namea+')'+'|'+'\n'
            myFile.write(a)
        pass
