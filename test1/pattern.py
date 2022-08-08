# 1,2,3,4
# 1,3  odd
# 2,4   even

initial=int(input("enter range"))
final=int(input("enter range"))
for i in range(initial,final):
    if i%2==0:
        for a in range(5,0,-1):
            for j in range(a):
                print(i,end=" ")
            print()
    else:
        for a in range(1,5):
            for j in range(a):
                print(i,end=" ")
            print()
1