# factorial

# 5!=5*4*3*2*1
# 3=1*2*3=6

num=int(input("enter a number"))
fact = 1
for i in range(1,num+1):
    fact=fact*i
    print(fact)

