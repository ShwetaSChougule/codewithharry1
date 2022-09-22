# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.no = eno
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print(self.no)
#         print(self.ename)
#         print(self.esal)
# class Test:
#     def modify(emp):
#         emp.esal= emp.esal  + 2000
#         emp.display()
# e = Employee(100,'Durga',10000)
#
# Test.modify(e)
#
# class Emp:
#     def __init__(self,name,id,salary):
#         self.name = name
#         self.id   = id
#         self.salary = salary
#     def how(self):
#         print('Name',self.name)
#         print('id',self.id)
#         print('salary',self.salary)
#
# class Test:
#     def modify(n):
#         n.salary = n.salary + 600
#         n.show()
#
# e = Emp('Shweta','2',3333)
# Test.modify(e)


# inner class:
# multiple inner class:
class Doc:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('I am outer class')
        print(self.name)

    class Dentist:
            def __init__(self):
                self.name = 'Dr.Savita'
                self.degree = 'BDS'
            def display(self):
                print('Name', self.name)
                print('Degree',self.degree)
    class Cardiologist:
            def __init__(self):
                self.name = 'Dr. Amit'
                self.degree = 'DM'

            def display(self):
                print("Name:", self.name)
                print("Degree:", self.degree)

outer = Doc()
inner1 = outer.den
inner2 = outer.car

inner1.display()
inner2.display()
