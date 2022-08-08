class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.agee=age
        self.place=place
    def printvalue(self):
        print(self.name,self.agee,self.place)
pe=Person("anu",23,"kochi")
pe.printvalue()

pe2=Person("alan",25,"kollam")
pe2.printvalue()
