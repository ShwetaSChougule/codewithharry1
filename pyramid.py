#
# n = int(input("Enter number of rows"))
# for i in range(n):
#     for j in reversed(range(n)):
#         print("*",end="")
#     print("\n" )
#     n -= 1
#
# for i in range(1,5,1):
#     print(i)
#
# for j in range(3):
#     print(j)

# for n in range(9,100,3):
#         print(n,"\n")
#
# 1
# 22
# 333

# n = int(input("Enter rows"))
# 1
# 22
# 333
# 4444
# 55555
# for i in range(n+1):
#     for j in range(i):
#         print(i,end="")
#     print("\n")


# 55555
# 4444
# 333
# 22
# 1


# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print("\n")

# for i in reversed(range(1,6)):
#     print(i)

# list1 = [23,45,56,67,78,55]
# print(list1[::-1])

# import numpy as np
# for i in np.arange(0,5,0.5):
#     print(i)

# y = 10
# while y<= 10:
#     print("Hi")
#     y = y + 1

# # Pyramid pattern:
#     *
#    ***
#   *****




# n = int(input("Enter number "))
# for i in range(n):
#   for j in range(i):
#       print("*",end=" ")
#   print("\n")

n = int(input("Enter rows"))
for i in range (n+1):
    print(" "*(n-i),"*"*(i))

n = int(input("Enter rows"))
for i in range(n+1):
    print("*"*i," "*(n-i))


n = int(input("Enter rows"))
for i in range(0,n+1):
    print(" "*(n-i),end="")
    print("* "*i)


n = int(input("Enter rows"))
import string
for i in range(1,n+1):
    print(" "*(n-i),string.ascii_lowercase[i-1]*i)

# import string
# print(string.ascii_lowercase[0])

n = int(input("Enter number of rows"))
import string
for i in range(n+1):
    print(string.ascii_lowercase[i-1]*i," "*(n-i))

n = int(input("Enter number of rows"))
for i in range(0,n+1):
    for j in range(i):
        print(i,end=" ")
    print("\n")

 #     1
 #    2 2
 #   3 3 3
 #  4 4 4 4
 # 5 5 5 5 5


n = int(input("Enter number of rows"))
for i in range(n):
    for j in range(i):
        # print((n-i)*" ",i)
        print((n-i)*" ",end="")
        print(i,end=" ")
    print("\n")
























