s=input("enter a string")
n=""
r=""
for i in s:
    if i not in n:
        n=n+i
    else:
        print(i)
        break