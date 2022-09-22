#to check if string is palindrome.
# n = input('Enter a string')


# name = "geeks FOR geeks"
#
# print(name.capitalize())
# print(name.title())

# reverse the words in given list
# s = 'Hi this is Shweta'
# o = []
# l = s.split()
# print(l)
# for i in l:
#     i = i[::-1]
#     o.append(i)
# print(o)
# print(' '.join(o))
# for i in l:
#     i = i[::-1]
#     print(i)
#     o.append(i)
# print(' '.join(o))

# even length words:
# s = 'Hi this is Shwetac'
# old = s.split()
# new = []
# for i in old:
#     print(i)
#     l = len(i)
#     if l%2 == 0:
#         new.append(i)
#
# print(new)
#
# import re
# str = '9049301579'
# m = re.fullmatch('[7-9][0-9]{9}',str)
# if m != None:
#     print('yes')

# #     operator overloading
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
# B1 = Book(200)
# B2 = Book(250)
# print(B1+B2)
# # method overloading
#
# class A:
#     def method1(self):
#         print('no arg')
#     def method1(self,a):
#         print('one arg')
#     def method1(self,a,b):
#         print('two arg')
#
# a = A()
# a.method1()

class A:
    def m1(self,a=2,b=3,c=4):
        if a!= None and b!=None:
            print(a+b)
        elif a!= None and b!=None and c!= None:
            print(a+b+c)
        else:
            print('give args')

m = A()
m.m1()
