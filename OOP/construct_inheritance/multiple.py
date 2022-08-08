class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent:
    def __init__(self,phn,adrs):
        self.phn=phn
        self.adrs=adrs
class Employee(Person,Parent):
    def __init__(self,id,desig,salary,name,age,place,phn,adrs):
        Person.__init__(self,name,age,place)
        Parent.__init__(self,phn,adrs)
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.name,self.age,self.place,self.phn,self.adrs,self.id,self.desig,self.salary)
emp=Employee(1,"dev",45000,"anu",28,"thrissur",6282198093,"abc")
emp.printEmployee()