class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent:
    def setparent(self,phn,adrs):
        self.phn=phn
        self.adrs=adrs
class Employee(Person,Parent):
    def setemployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.name,self.age,self.place,self.phn,self.adrs,self.id,self.desig,self.salary)
emp=Employee()
emp.setemployee(1,"dev",56000)
emp.setparent(6282198093,"aabc")
emp.setperson("amal",26,"kochi")
emp.printEmployee()
