# #simple class
class animal:
    '''This class represents doc string'''
    species = 'Dog'
    def __init__(self,name,color):
        self.name  = name       #instance variable
        self.color = color

    def breed(self,breed):
        self.breed = breed
    def display(self):
        print('Category is {},\nname is {},\ncolor is {}'.format(animal.species,d.name,d.color))

d = animal('Tommy','Black')
d.display()
print(animal.__doc__)
#
#
# class Employee:
#     def __init__(self,roll,name):
#         self.roll = roll
#         self.name  = name
#
# e = Employee(44,'shweta')
# # print(e.__dict__)
# #
# class Test:
#     def __init__(self,maths,science):
#         self.maths = maths
#         self.science = science
#
#     def dis(self):
#         self.phy = 45
#
# t = Test(40,34)
# t2 = Test(55,77)
# t.marathi = 66
# del t.marathi
#
# t.dis()
# t2.dis()
#
# print(t.__dict__)

#
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print("Hi",self.name)
#     def grade(self):
#         if self.marks > 60:
#             print('First class')
#         else:
#              print('Second class')
# num = int(input('Enter number of students'))
# for i in range(num):
#     n = input("Enter name")
#     m = int(input("Enter marks"))
#     s = Student(n,m)
#     s.display()
#     s.grade()
#
# class Student:
#     def setName(self,name):
#         self.name = name
#     def getName(self,name):
#         return self.name
#     def setMarks(self,marks):
#         self.marks  = marks
#     def getMarks(self,marks):
#         return self.marks
#
# n = int(input('Enter number of students'))
# for i in range(n):
#     s = Student()
#     n = input('Enter name')
#     s.setName(n)
#     m = int(input('Enter marks'))
#     s.setMarks(m)
#
#     print('Hi',s.getName(n))
#     print('Marks',s.getMarks(m))
#
# # WORKING
# class Student:
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#
# n = int(input("Enter number of students"))
# for i in range(n):
#     s = Student()
#     name1 = input("Enter name of student")
#     s.setName(name1)
#
#     print('Hi',s.getName())

# Class methods:
# class variables.



# Class method
# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls,name):
#         print('{} has {} legs'.format(name,Animal.legs))
#
# a = Animal()
# a.walk('Tommy')


# Static method:
import gc


class sta:
    @staticmethod
    def add(x,y):
        print('Sum is',x+y)


sta.add(3,6)

gc.isenabled()
#gc is by default on, to check gc.isebabled()
# gc.ena

# destroctors:
#special method  name del


