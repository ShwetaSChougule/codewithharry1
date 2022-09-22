def outer(func):
    def inner(*args):
        print(func(*args))
    return inner

@outer
def addition(a,b):
    return a+b

addition(4,5)

