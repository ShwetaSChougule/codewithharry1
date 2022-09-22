# # returning functions:
# def parent(num):
#     def child1():
#         return "I am Shweta"
#
#     def child2():
#         return "I am Sham"
#
#     if num == 1 :
#         print(child1())
#     else:
#         print(child2())
# parent(1)


# # Assign a function to a variable
# def fun(x):
#      return x.upper()
#      print(x.upper())
# fun("shweta")
#
# a = 4
# b = 5
# c = sum((a,b))
# # print(c)
# #
# # numbers = [1,2,3,4]
# # sum = sum(numbers,10)
# # print(sum)
#
# def f2(x,y):
#     ave = (x+y)/2
#     print(ave)
#
#     a2 = type(ave)



# def summ(a,b):
#     print(a+b)
#
# summ(1,2)

#
# def summ(a,b):
#     c = a+b
#     print(c)
#
# print(summ(2,3))
#


# def summ(e,t):
#     sum = e + t
#     return sum
#
# a = summ(2,3)
# print(a)

def fact(n):
    """Calculate factorial of number"""

    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        else:
            return n * fact(n-1)
    else:
        raise TypeError("n should be integer and n >=0")

f = fact(5)
print(f)











