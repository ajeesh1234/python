def sum_prime(initial,final):
    sum=0
    for i in range(initial,final+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum=sum+i
    return (sum)
print(sum_prime(3,19))