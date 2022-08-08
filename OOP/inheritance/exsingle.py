# person name,age,place
# student roll,deprt

class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstudent(self,roll,dep):
        self.roll=roll
        self.dep=dep
    def printvaluestudent(self):
        print(self.name,"roll no is",self.roll)
        print(self.dep)
st=Student()
st.setstudent(1,"bca")
st.setvalue("anu",22,"kochi")
st.printvalue()
st.printvaluestudent()