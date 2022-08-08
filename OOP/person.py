class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.agee=age
        self.place=place
    def printvalue(self):
        print(self.name,self.agee,self.place)
pe=Person()
pe.setvalue("anu",23,"kochi")
pe.printvalue()

pe2=Person()
pe2.setvalue("alan",22,"kollam")
pe2.printvalue()
