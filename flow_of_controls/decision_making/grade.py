score=int(input("enter your score"))
if score<=100:
    if score>=90:
        print("A+")
    elif score>=80:
        print("A")
    elif score>=70:
        print("B+")
    elif score>=60:
        print("B")
    elif score>=50:
        print("C+")
    else:
        print("Fail")