# stack
# push = elements add
# pop = elements remove

stack=[]
size=int(input("enter size"))
top=0

def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter element to add"))
        stack.append(e)
        top=top+1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print('stack is empty')
    else:
        stack.pop()
        top = top - 1
        print(stack)
while True:
    print("enter the option\n1.push\n2.pop\n")
    option = int(input("enter"))
    if option == 1:
        push()
    elif option == 1:
        pop()
    else:
        print("invalid")

