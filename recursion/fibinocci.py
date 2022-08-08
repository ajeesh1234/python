# fibinocci
# 0  1 1 2 3

def fibinocci(n):                         #n=4
    if n<=1:
        return n
    else:
        return fibinocci(n-1)+fibinocci(n-2)
                                            # fibinocci(3)+fibinocci(2)=2+1=3
for i in range(10):
    print(fibinocci(i))