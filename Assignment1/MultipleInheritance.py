# single inheritances
# class A:
#     def classA(self):
#         print('This is class A')
# class B(A):
#     def classB(self):
#         print('This is class B')
#
# obj = B()
# obj.classB()
# obj.classA()

# # # Multiple Inheritence
# class A:
#     var = 1
#     def classA(self):
#         print('This is class A')
# class B:
#     var = 2
#     def classB(self):
#         print('This is class B')
# class C(A,B):
#     pass
#
# c = C()
# c.classA()
# c.classB()
# print(c.var)
#
# # Multilevel
class A:
    f = 4
    def classA(self):
        print('This is class A')
class B(A):
    def classB(self):
        print('This is class B')
class C(B):
    def classC(self):
        print('This is class C')
    def classB(self):
        print('New class B')

darry = A()
larry = B()
harry = C()
harry.classB()
print(harry.f)
