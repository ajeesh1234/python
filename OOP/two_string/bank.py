class Bank:
   bank_name="SBI"
   def ac_create(self,name,accno):
       self.name=name
       self.accno=accno
       self.minbalce=5000
       self.balance=self.minbalce
   def deposit(self,amnt):
       self.amt=amt
       self.balance=self.balance+self.amnt
       print("your",Bank.bank_name,"ac has been credited with amount,",self.amnt)
       print("your current balance is",self.balance)
   def witdraw(self,amnt):
       self.amnt=amnt
       if self.amnt<self.balance:
           self.balance=self.balance-self.amnt
           print("your",Bank.bank_naame,"ac has been debited with amount",self.amnt)
           print("your current account balance is",self.balance)
       else:
           print("your current account balance is", self.balance)

