s=input("enter a string")
n=""
r=""
for i in s:
    if i not in s:
        n=n+i
    else:
        r=r+i
print("recurssive elements are",r)
print("unique elements are,n")

