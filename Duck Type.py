
# Duck Type Philosophy
class A:
    def __init__(self):
        pass
    def method1(self):
        print('This is Class A')

class B:
    def __init__(self):
        pass
    def method1(self):
        print('This is Class B')

def func(obj):
    obj.method1()

# a = [A(),B()]
# for i in a:
#     func(i)

for i in A(),B():
    i.method1()

# pip list
