# pallindrome checking using function
# function without argument

def pallindrome():
    s=input("enter a string")
    r=s[::-1]
    if s==r:
        print("pallindrome")
    else:
        print("not pallindrome")
pallindrome()