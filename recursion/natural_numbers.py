# 5
# 0+1+2+3+4+5

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(3))
print(sum(5))