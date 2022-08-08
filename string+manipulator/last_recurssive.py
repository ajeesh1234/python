s=input("enter a string")
n=""
r=""
for i in s:
    if i not in n:
        n=n+i
    else:
        r=r+i
print(r[-1])