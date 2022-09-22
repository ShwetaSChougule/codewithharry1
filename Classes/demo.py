# class Dog:
#     '''This class gives details about dogs'''
#     species = 'Mammal'
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#         del self.color
#     def show(self):
#         print(f"Name is {self.name} and color is {self.color}")
#
# Tom = Dog('Tom','Black')
# Tuffy = Dog('Tuffy','Brown')
# Tom.show()
# Tuffy.show()
# print(Tom.__dict__)
# print(Tuffy.__dict__)
# print(Tom.species)
# # print(Dog.__doc__)
# # help(Dog)
#
#
# # Constructor
#
#
#
#
#
# # f string example
#
# # name = 'Shweta'
# # age = '30'
# # print(f"Hello, this is {name},I am {age} years old")
# #
# #
# #
#
# # chr(): to get character based on unicode provided
# # ord(): to get unicode based on char
# # newline = ord('\\')
# # print(newline)
#
# # datetime:
# # import datetime
# # todaydetails = datetime.datetime.today()
# # print(f"{todaydetails:%B %d, %Y}")
#
# getter and setter:
# def init:
#     self.name = name
# syntax: def setVar(self,var):
#                 self.var = var
#
# class student:
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#
# s = student()
#
# n = input('Enter number of students')
# for i in n:
#     name = input('Enter name')
#     s.setName(name)
#
#     print(s.getName())
#
# class method:
#
# class Dog:
#     species = 'Animal'
#     @classmethod
#     def display(cls,name):
#         print(f'Dog is an {cls.species} and name is {name}')
#
# Dog.display('Tommy')
#
#

# class method:
class Shweta:
    age = '30'
    @classmethod
    def show(cls,role):
        print(f'Name is sana, age is {cls.age} and role is {role}')

Shweta.show('student')