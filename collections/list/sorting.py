# l=[1,3,2,5,6,4]
# l.sort()
# print(l)

l=[6,4,7,2,1,3]
n=[]
while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    n.append(min)
    l.remove(min)
print(n)
print(l)