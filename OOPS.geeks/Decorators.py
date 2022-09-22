# Decorators allows programmers to modify the behaviour of a function or a class.
# Decorators allow us to wrap another function to extend behaviour of wrapped function ,
# without permanantly modifying it.

# Python supports first class object concept:
#1. we can store function in variable.
#
# def upper_letter(text):
#     return text.upper()
#
# var = upper_letter         #It takes a function object referred by upper_letter
# print(var('Shweta'))

# 2.We can pass function as parameter to another function.
# we can pass a function as an argument to another function.
# Functions that accept another function as an arguments are called as Higher-order function.
#
# def upper_letter(text):
#     return text.upper()
# def lower_letter(text):
#     return text.lower()
#
# def modify(func):
#     var = func('We are learning python')
#     return var
#
# print(modify(upper_letter))
#
#
# # 3.Functions can return another function
# def adding(x):
#     def inner(y):
#         return x+y
#     return inner
#
# z = adding(5)
# print(z(10))


#Decorators:
# def hello_decorator(func):
#     def inner():
#         print('This is before function execution')
#         func()
#         print('This is after function execution')
#     return inner
#
# def main_function():
#     print('This is main function')
#
#
# main_function = hello_decorator(main_function)
#
# main_function()

# USING DECORATORS TO CALCULATE TIME TAKEN BY A FUNCTION:
# import time
#
# def time_cal(func):
#     def inner():
#         start = time.time()
#         func()
#         time.sleep(3)
#         end = time.time()
#         print('Time taken by ,', func.__name__, end - start)
#     return inner
#
# @time_cal
# def cal_power():
#     print(10**5)
#
# cal_power()

# WHEN INNER FUNCTION RETURNS VALUE
# def deco(func):
#     def inner(*args,**kwargs):
#         print('Before Execution')
#         ret_value = func(*args,**kwargs)
#         print('After Execution')
#         return ret_value                     #inner fn returns value
#     return inner                             #deco returns value
#
# @deco
# def sum_num(a,b):
#     print(a+b)
#
# print(sum_num(4,5))

# arg means tuple of positional arguments
# kwargs means dictionary of keyword arguments

#DECORATOR CHAINING:
#Applying more than one decorator to a function.
#
# def dec1(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner
#
# def dec2(func):
#     def inner1():
#         x = func()
#         return x*2
#     return inner1
#
# @dec1
# @dec2
# def f():
#     return 10
# print(f())

# DECORATOR FOR ERROR HANDLING
def err_handler(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print(f"{func.__name__} has wrong data types")
    return inner

# @err_handler
# def adding(a,b):
#     return (a+b)/2
#
# print(adding(0,0))

@err_handler
def adding(a,b):
    print((a+b)/2)

adding('a','b')

