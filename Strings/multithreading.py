
from threading import *
class Abc:
    def show(self):
        for i in range(10):
            print('Hi')

a=Abc()
t1 = Thread(target= a.show)
t1.start()
for i in range(10):
    print('Team brainworks')

