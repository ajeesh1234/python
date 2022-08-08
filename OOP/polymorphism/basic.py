# polymorphism
# poly means many
# morph means form

# method overiding
# method overloading

# method overloading

class A:
    def printdata(self,num1):
        self.num1=num1
        print(self.num1)
class B(A):
    def printdata(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print(self.no1,self.no2)
objb=B()
objb.printdata(6,7)
objb.printdata(6)