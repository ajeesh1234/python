# strin_manipulation


# s="Luminar Technolab"
# for i in s:
#     print(i)


s="Luminar Technolab"
flag=0
for i in s:
    if i=='a':
        flag=1
        break
if flag==1:
    print("present")
else:
    print("not present")

    # 3rd method

    # for i in s:
    #     if i=='a':
    #         print("present")
    #         break
    #
    # else:
    #     print("not present")

    # 4th method
    # if 'a' in s:                  if 'z' not in s:
    #     print("present")                 not present
    # else:
    #     print("not present")


