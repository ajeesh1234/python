age=int(input("enter age"))
if age<18:
    raise Exception("not eligable")
else:
    print("eligable")