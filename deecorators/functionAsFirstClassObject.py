#function as object:
#
# def upperletter(n):
#     return n.upper()
#
# letter = upperletter
#
# print(letter('Shweta'))

# function as argument: example1
# def letterupper(n):
#     return n.upper()
#
# def modification(func):
#     obj = func('Hi there')
#     print(obj)

# modification(letterupper)

# example2:
# define function
# def square(n):
#     return n**2
# # iterable
# l1 = [2,3,4,5,6]
#
# def sq_func(fun,l):
#     res = [fun(i) for i in l1]
#     return res
#
# sq_func(square,1l)

# returning a function
# def adding(x):                    #first
#     def inner(y):                 #second
#         return x+y
#     return inner
#
# obj = adding(5)
# print(obj(6))
#
#
# def upletter(n):
#     return n.upper()
#
# def modification(func):
#     obj = func('hello')
#     print(obj)
#
# modification(upletter)

#
# class Student:
#     sclass = '2'                  #class variable
#     def __init__(self,sid,name):
#         self.name = name            #instance variable
#         self.sid =sid
#     def display(self):
#         print('Id is',self.sid)
#         print('name is',self.name)
#         print('class is',Student.sclass)
#
# obj = Student(23,'Shweta')
# obj.display()
#


# deco

# def deco(func):
#     def inner():        #wrapper
#         func()          #actual function
#     return inner
#
# def fun():
#     print('Hi')
#
# fun = deco(fun)
# fun()



# def deco(func):                 #function
#     def inner():                #pass the arguments
#         func()
#     return inner
#
# def fun():                       #actual function defining
#     print('something')
#
# fun = deco(fun)
# fun()
# import time
# import math

# def cal(func):
#     def inner(n):
#         begin = time.time()
#         func()
#         end = time.time()
#         print(end-begin)
#     return inner
#
# def powerof(n):
#     print(n**234)
#
# powerof = cal(powerof)
# powerof(5)
import time


# def deco(func):
#     def inner():
#         func()
#
#     return inner
#
# @deco
# def mainfunc():
#     print('HI')
#
# mainfunc()

# import time
#
# def calc(func):
#     def inner(n):
#         start = time.time()
#         func(n)
#         end = time.time()
#         print(round(end-start,2))
#     return inner
#
# @calc
# def mainfn(n):
#     print(n**68)
#
# mainfn(45)


# from time import time
#
# def timecal(func):
#     def inner(n):
#         start = time.time()
#         func(n)
#         end = time.time()
#         print(end-start)
#     return inner
#
# @timecal
# def mul(n):
#     print(n**456)
#
# mul(55)
#
# def reversedec(func):
#     def inner():
#         r  = sorted(func())
#         print(r)
#     return inner
#
# @reversedec
# def mainfn(n):
#     print('input is',n)
#
# print(mainfn('Hi'))
#






