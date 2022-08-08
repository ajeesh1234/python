# queue

queue=[]
size=int(input("enter size"))
top=0

def enqueue():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter element to add"))
        queue.append(e)
        top=top+1
        print(queue)
def dequeue():
    global top,size
    if top<=0:
        print('queue is empty')
    else:
        queue.remove(queue[0])
        top = top - 1
        print(queue)
while True:
        print("enter the option\n1.enqueue\n2.dequeue\n")
        option = int(input("enter"))
        if option == 1:
            enqueue()
        elif option == 1:
            dequeue()
        else:
            print("invalid")
