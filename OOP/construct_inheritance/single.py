class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll,dep,name,age,place):
        super().__init__(name,place,age)
        self.roll=roll
        self.dep=dep
    def printstudent(self):
        print(self.roll)
        print(self.dep)
st=Student(1,"cse","anu",23,"kochi")
st.printperson()
st.printstudent()