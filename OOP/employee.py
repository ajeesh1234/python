class Employee:
    def setvalue(self,name,id,desig,salary,company_name):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
        self.company_name=company_name
    def printemployee(self):
        print(self.name)
        print(self.id)
        print(self.desig)
        print(self.salary)
        print(self.company_name)
emp1=Employee()
emp1.setvalue("anu",1,3700,"dev","luminar")
emp1.printemployee()