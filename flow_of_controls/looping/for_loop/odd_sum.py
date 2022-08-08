initial=int(input("enter the range 1"))
final=int(input("enter the range 2"))
sum=0
for i in range(initial,final):
    if i%2!=0:
        sum+=i
        print(sum)
