num = int(input("Enter number"))
def rec(num):
    return (num * rec(num-1))

result = rec(num)
print("Factorial is",result)

# Not working
