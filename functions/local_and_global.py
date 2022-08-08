# local variable and global variable

def printx():
    global x,n
    n=5
    x=10
    print(x)
printx()
print(x,n)