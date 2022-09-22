n = int(input("Enter the number"))
# Define number out of function
def fact1(n):
    fact1 = 1
    if (n<0):
        return ("Error")
    elif (n==0):
        return ("1")
    else:
        for i in range(1,n+1):
            fact1 = fact1 * i
        return fact1
print(fact1(n))