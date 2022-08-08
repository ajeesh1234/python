# linear searching

l=[1,3,6,7,9,0,4,54,39,62,88]
def linear_search():
    e=int(input("enter element to search"))
    for i in l:
        if i==e:
            print("found")
            break
    else:
        print("not found")
linear_search()