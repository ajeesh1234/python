# 1 to 10
# 2,4,6,88,10

# METHOD 1

# for i in range(1,11):
#     if i%2==0:
#         print(i)

# METHOD 2

initial=int(input("enter initial range"))
final=int(input("enter final range"))
for i in range(initial,final):
    if i%2==0:
        print(i)