l=[1,3,5,7,2,4]
# sort
# [1,2,3,4,5,7]
# [4,5,7]
# [4]

e=int(input("enter element to search"))
flag=0
l.sort()
low=0
upper=len(l)-1
while low<=upper:
    middle_index=(low+upper)//2
    if l[middle_index]==e:
        flag=1
        break
    elif e>l[middle_index]:
        low=middle_index+1
    elif e<l[middle_index]:
        upper=middle_index-1
if flag==1:
    print("found")
else:
    print("not found")