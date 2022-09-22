#Notes
# Decorators are a very powerful and useful tool in Python
# since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of
# the wrapped function, without permanently modifying it.

# syntax:
# def dec(func):
#     def inner():
#         print('Before')
#         func()
#         print('after')
#     return inner
#
# def func_used():
#     print('this is func')
#
# func_used = dec(func_used())
#
# func_used()


# Addition of new number in a decorator
# def dec(func):
#     def inner():
#         n3= int(input('Enter a number'))
#         r1 = func()
#         r1 = r1 + n3
#         print(r1)
#         return r1
#     return inner
# @dec
# def addn():
#     n1= int(input('Enter a number'))
#     n2= int(input('Enter a number'))
#     return n1+n2
# addn()


# Time calculation in python
# import time
#
# def cal(func):
#     def inner():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print('Difference is',t2-t1)
#     return inner
#
# @cal
# def p():
#
#     time.sleep(2)
#     print('Hi')
# p()


#Python closures:
# when inner fn that are enclosed in outer fn,
#closure is access variables present in the outer function scope,
#it can access variables ,even if outer fnhas completed execution

# A Closure is a 'function object' that remembers values in enclosing scopes even
# if they are not present in memory.
# def outer():
#     message = 'Hi'
#
#     def inner():
#         print(message)
#     return inner
#
# obj = outer()

# obj is that fn object

# use of closures:It can be used for code re-usability as class but in smaller extent.
# If we have to make sq,cube of anything

# def to_power(n):   #power
#     def num(x):    #number
#         return x**n
#     return num
#
# a = to_power(2)
# print(a(3))

#####################################################
#Difference between inner() and inner
# def outer():
#     def inner(*args):
#         a = 3+7
#         print(a)
#     return inner()   #it will give us calculated value of inner fun.
#
# obj = outer()
# obj


# def outer():
#     def inner():
#         a = 3+7
#         print(a)
#     return inner      #it will give us inner function as object
#
# obj = outer()
# obj()


#deco to avoid zero div
def decor(func):
    def inner(a,b):
        if b==0:
            print('zero division not possible')
        else:
            print(func(a,b))
    return inner
@decor
def div(a,b):
    return a/b

div(3,0)