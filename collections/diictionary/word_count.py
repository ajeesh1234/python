s=input("enter a string")
d={}
data=s.split(" ")
for i in data:
    if i not in d:
        d.update({i:1})
    else:
        val=d[i]
        val+=1
        d.update({i:val})
print(d)

# {"hello":2,"hi":1}

# data=s.split(" ")
# print(data)