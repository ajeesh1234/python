# decorators

def changevalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@changevalue
def sub(n1,n2):
    print(n1-n2)
@changevalue
def div(n1,n2):
    print(n1/n2)
div(2,3)