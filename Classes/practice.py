class Person():
    def __init__(self,name,c):
        self.name = name
        self.c = c

    def show(self):
        print(f'Name is {self.name} and children are {self.c}')

obj = Person('Saroj','2')
obj.show()

class Shweta(Person):
    def __init__(self,name,c,age):
        super().__init__(name,c)
        self.age = '30'

    def display(self):
        print(f'Age is,{self.age}')

obj1 = Shweta('Shweta','0','30')
obj1.show()
obj1.display()