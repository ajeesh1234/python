class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printperson(self):
f=open('person1.txt','r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    per=Person(name,age)
    per.printperson()