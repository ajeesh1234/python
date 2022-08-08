students=[('anu',67),("amal",69),("akhil",65)]
marks=[]
for i in students:
    marks.append(i[1])
maximum=max(marks)
for i in students:
    if i[1]==maximum:
        print(i)