# student...name,roll no,dept,college

class Student:
    def setstudent(self,name,rollno,dept,college):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.college=college
    def printstudent(self):
        print(self.name)
        print(self.rollno)
        print(self.dept)
        print(self.college)
st1=Student()
st1.setstudent("anu",23,"bcom","luminar")
st1.printstudent()