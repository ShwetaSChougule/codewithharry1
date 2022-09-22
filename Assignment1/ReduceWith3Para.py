# def sq(n):
#     i =1
#     while i<n:
#         yield i*i
#         i+=1
#
# x = sq(10)
#
# for i in x:
#     print(i)

def fib(n):
    a = 0
    b = 1
    while a<n:
            yield a
            a = b
            b = a+b

x = fib(5)
for i in x:
    print(i)



