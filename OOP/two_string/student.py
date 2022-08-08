class Student:
   def __init__(self,name,roll,dept):
        self.name=name
        self.roll=roll
        self.dept=dept

f = open('student.txt', 'r')
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    roll = data[1]
    dept = data[2]
    st= Student(name,roll,dept)
    st.printstudent()