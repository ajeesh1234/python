class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
      print(self.name,self.age,self.place)
    def __str__(self):
        return str(self.age)
pe=Person("anu",22,"kochi")
print(pe)