# inheritance
#single inheritance

class A:       #parent class/Base class/super class
    def printa(self,a):
        self.a=a
        print("inside A",self.a)
class B(A):    #child class/sub class/derived class
    def printb(self,b):
        self.b=b
        print("inside B",self.b,self.a)
objb=B()
objb.printa(5)
objb.printb(7)

obja=A()
obja.printa(9)
