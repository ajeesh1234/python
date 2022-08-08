# l=[1,2,3,4,5,6,7]
# l[1]=100
# l[3:5]=[100,200]
# print(l)

l=[1,2,3,4,5,6,7]
middle_index=len(l)//2
l.remove(l[middle_index])
print(l)
