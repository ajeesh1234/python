# constructors

class Add:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def findvalue(self):
        print(self.n1+self.n2)
ad=Add(100,200)
ad.findvalue()