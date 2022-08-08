def usercheck(func):
    def wrapper(a,b):
        if a=="admin":
            return (a,b)
        else:
            raise Exception("not allowed")
    return wrapper

@usercheck
def password(pin):
    mypin=pin
    return mypin
print(password("user",555))
