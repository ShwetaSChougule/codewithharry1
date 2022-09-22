# Factorial using recursion
n= int(input('Enter a  number'))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

if n <0:
    print('error')
elif n == 0:
    print(1)
else:
    print(fact(n))

# Memoization: