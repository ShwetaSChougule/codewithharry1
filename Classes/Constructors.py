#Constructor in python
# Default constrictor:
class Greeting:
    def __init__(self):
        self.name = 'Shweta'
    def Display(self):
        print('Hi {}'.format(self.name))

obj = Greeting()
obj.Display()

# Parameterized constructor
class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def cal(self):
        self.answer = self.first + self.second
    def dis(self):
        print('Addition is',self.answer)

obj = Addition(2,3)
obj.cal()
obj.dis()