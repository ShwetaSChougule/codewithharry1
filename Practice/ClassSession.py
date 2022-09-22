class Abc:
    def __init__(self):
        print("Today")
    def xyz(self):
        print("i am parent class")
    def mnr(self):
        print("Team Brainworks")

class Pqr(Abc):
    def __init__(self):
        print("2022")
    def abc(self):
        print("Hello")
    def xyz(self):
        super().xyz()
        print("hi")

a = Pqr()
a.xyz()
a.mnr()
a.abc()

# 2022
# I am parent classmethod
# hi
# team
# Hello