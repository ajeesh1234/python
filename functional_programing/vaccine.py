def agevalidate(func):
    def wrapper(a,b):
        if b>=18:
            return func(a,b)
        else:
            raise Exception("not allowed")
    return wrapper

@agevalidate
def vaccinate(name,age):
    return "vaccinated"
print((vaccinate("anu",15)))



