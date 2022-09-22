# Factorial without recurssion
# num = int(input('Enter a number'))

# def factorial(n):
#     fact = 1
#     if n <0:
#         print('Enter valid input')
#     elif n==0:
#         print('Factorial is 1')
#     else:
#         for i in range(1,n+1):
#             fact = fact * i
#         print(fact)
#
# factorial(num)

# fact 0 and fact 1 are 1

def recu(n):
    if n == 1:
        return 1
    else:
        return n* recu(n-1)


num = int(input('Enter a number'))
if num < 0:
    print('Enter a valid number')
elif num==0:
    print('1')
else:
    print('Fact is ',recu(num))
    





