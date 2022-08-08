l1=[1,3,5,7,9,5,3,1,2,3,4,5,6]
n=[]
n2=[]
for i in l1:
    if i not in n:
        n.append(i)
    else:
        if i not in n2:
            n2.append(i)
print(n2)
    