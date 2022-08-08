# exception_handling

num1=int(input("enter num1"))
num2=int(input("enter num2"))
try:
    print("inside try")
    print(num1/num2)
except Exception as e:
    print("exception occured",e)
finally:
    print("inside finally")

# try
# except
