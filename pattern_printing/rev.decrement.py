k=8
for i in range(5):
    for s in range(k):
        print(end=" ")
    k=k-2
    for j in range(i):
        print("*",end=" ")
    print()