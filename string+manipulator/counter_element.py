# s=aaabbbcccc
s="aaabbbcccc"
e=input("enter a element")
count=0
for i in s:
    if i in e:
        count=count+1
        print(count)