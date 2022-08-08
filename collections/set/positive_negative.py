# s={1,2,3,4,5,-1,-2,-3,-4,-5}
# for i in s:
#     if i>0:
#         print("pos")
#     if i<0:
#         print("neg")

s={1,2,3,4,5,-1,-2,-3,-4,-5}
positive=set()
negative=set()
for i in s:
    if i>0:
        positive.add(i)
    else:
        negative.add(i)
print(positive)
print(negative)


