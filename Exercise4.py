
# def pattern(n,a):
n = int(input("Enter a number"))
a = int(input("0 or 1"))

if a==0 or a==1:
    b = bool(a)
    if b == True:
        i = 1
        for i in range(n):
            for j in range(i):
                print("*", end="")
            print("\n")

    elif b == False:
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print("\n")
            n = n - 1
else:
    print("Enter valid value for a")
    a = int(input("0 or 1"))
    # pattern(n,a)