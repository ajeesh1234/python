class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Child(Person):
    def setchild(self,phn,adrs):
        self.phn=phn
        self.adrs=adrs
class Student(Child):
    def setstudent(self,roll,deprt):
        self.roll=roll
        self.deprt=deprt
    def printvalues(self):
        print(self.name,self.age,self.place,self.phn,self.adrs,self.roll,self.deprt)
st=Student()
st.setperson("anu",22,"thrissur")
st.setchild(6282198093,"aabc")
st.setstudent(1,"bca")
st.printvalues()
