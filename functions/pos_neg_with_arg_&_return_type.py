def pos_neg(number):
    if number>0:
        return("positive")
    elif number==0:
        return("zero")
    else:
        return("negative")
print(pos_neg(0))
print(pos_neg(-4))
print(pos_neg(10))