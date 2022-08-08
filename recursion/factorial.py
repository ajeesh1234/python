# n=3 3,2,1
# 1,2,3

def rec_factorial(n):
    if n==1:
        return 1
    else:
        return n*rec_factorial(n-1)
                                    # 3*rec_factorial(2)=3*2=6
                                    # 2*rec_factorial(1)=2*1=2
print(rec_factorial(3))