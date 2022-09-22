# x = lambda a:a+10
# print(x(1))
#
# x = lambda a,b:a+b
# print(x(2,3))
import functools
x = [3,4,5,6,7]
r = functools.reduce((lambda a,b:a+b),x)
print(r)

