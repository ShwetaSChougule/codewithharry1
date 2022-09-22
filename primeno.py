#Prime Number

num = int(input("Enter a number"))
n = 10
for x in range(2,n) :
    a = (num % x)
    if a == 0:
        print("Number is not prime")
        break
    else:
        print("Number is prime number")
        break
