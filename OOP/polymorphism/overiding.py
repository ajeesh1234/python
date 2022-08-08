# overiding
# same method name
# no:of arguments same

class A:
    def printdata(self,num1):
        self.num1=num1
        print("inside A",self.num1)
class B(A):
    def printdata(self,no1):
        self.no1=no1
        print("inside B",self.no1)
objb=B()
objb.printdata(5)