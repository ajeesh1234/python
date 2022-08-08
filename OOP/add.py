class Add:
    def inputvalue(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def findvalue(self):
        print(self.n1+self.n2)
ad=Add()
ad.inputvalue(100,200)
ad.findvalue()