#Single inher
import re


class A:
    def classA(self):
        print('This is class A')
class B(A):
    def classB(self):
        print('This is class B')
obj = B()
obj.classA()
obj.classB()

# multiple
class A:
    def m1(self):
        print('This is class A method1')
class B:
    def m2(self):
        print('This is class B method2')
class C(A,B):
    def m3(self):
        print('This is class C method')

obj = C()
obj.m1()
obj.m2()

# multilevel
class A:
    def classA(self):
        print('class A')

class B(A):
    def classB(self):
        print('class B')
class C(B):
    def classC(self):
        print('class C ')


obj = C()
obj.classA()

# hierarchical

# str = '0101010'
# m = re.compile('[^01]')
class A:
    def classA(self):
        print('this is class A')

class B(A):
    def classB(self):
        print('this is class B')
class C(A):
    def classC(self):
        print('this is class C')

o = B()
o1 = C()
o.classA()
o1.classC()
o1.classA()

# hybrid
# Encapsulation
# protected
class A:
    def __init__(self):
            self._a = 4


class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._a)
        self._a = 55
        print(self._a)

o = B()
o1 = A()

#use of super :used in constructor overriding
class A:
    def __init__(self,name,age):
        self.name = name
        print('Name is', self.name)
        self.age = age
        print('Age is', self.age)
        self.special = 'special'

class B(A):
    def __init__(self,name,age,city):
        super().__init__( name,age)
        self.city = city
        print('City is', self.city)

o = A('Shweta','30')
o1 = B('Shweta','30','Sangli')
print(o1.special)







