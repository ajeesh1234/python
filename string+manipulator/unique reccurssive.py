s=input("enter a string")
n=""
r=""
for i in s:
    if i not in n:
        n=n+i
    else:
        if i not in r:
            r=r+i
print(r[2])