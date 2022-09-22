#Inheritance allows us to define a class that inherits all methods and prop from another class.
# Methods and prop of parent class gets inherited to child class.

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print('Full name',self.firstname,self.lastname)
#
# obj = Person('Shweta','Chougule')
# obj.printname()
#
# class Student(Person):
#     # pass                                #pass is used when, we do not have to add any methods to class
#     def __init__(self,fname,lname,age):
#         # Person.__init__(self,fname,lname)
#         super().__init__(fname,lname)
#         self.age = '30'
#
# obj1 = Student('Sara','Khan',30)
# obj1.printname()


# Single Inheritance:
# Simple inheritance:
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def Show(self):
#         print('Name is',self.name)
#
# obj = Dog('Tommy')
# obj.Show()
#
# # Child
# class breed(Dog):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = 'Bulldog'
#     def dis(self):
#         print('Breed is',self.breed)
# obj1 = breed('Tommy','Bulldog')
# obj.Show()
# obj1.dis()


# Simple inheritance:
class Parent:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def Show(self):
        print('Name of parent',self.name)
        print('Parents are from',self.city)

# obj = Parent('Saroj','Sangli')

class Child(Parent):
    def __init__(self,name,city,cage):
        self.name = name
        self.age = cage
        Parent.__init__(self,name, city)


    def Display(self):
        print('Child\'s name is',self.name)
        print('Child\'s age is',self.age)
obj1 = Child('Shweta','Sangli','30')
obj1.Display()

