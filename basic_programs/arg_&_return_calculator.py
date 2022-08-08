def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
while True:
    option=int(input("select operation\n1.add\n2.sub\n3.mul\n4.div\n5.stop"))
    if option==5:
        break
    else:
        num1=float(input("enter num1"))
        num2=float(input("enter num2"))
        if option==1:
            print(add(num1,num2))
        elif option==2:
            print(sub(num1,num2))
        elif option==3:
            print(mul(num1,num2))
        elif option==4:
            print(div(num1,num2))
        else:
            print("invalid option")