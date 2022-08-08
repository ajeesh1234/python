k=8
for i in range(5):
    for s in range(k):
        print(end=" ")
    k=k-1
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for s in range(k):
        print(end=" ")
    k=k+1
    for j in range(i):
        print("*",end=" ")
    print()