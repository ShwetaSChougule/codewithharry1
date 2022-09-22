
#Pattern 1
# n = int(input('Enter number of rows'))
# for i in range(n+1):
#
#     for j in range(i):
#          print('*',end='')
#     print('\n')

# #Patterrn 1 approach2
# n = int(input('Enter a number'))
# c = 5
# for i in range(1,n+1):
#     print('*'*i)

#Pattern 2
# n = int(input('Enter a number'))
# for i in range(0,n):
#     print('*'*(n-i))
#     print('\n')

# Pattern3
# r = int(input('Enter rows'))
# l = int(input('Enter columns'))
# for i in range(0,r):
#     print('*'* l)

# Pattern 4
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# n = int(input('Enter number'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end='')
#     print()

#Pattern 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# n = int(input('Enter number'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end='')
#     print()

#Pattern 6
# A
# BB
# CCC
# DDDD
# # EEEEE
# n = int(input('Enter number'))
# num = 65
# for i in range(0,n):
#     for j in range(i+1):
#         ch = chr(num)   #returns character that represents specified unicode
#         print(ch,end='')
#     num += 1
#     print()
#
# # To return the integer that returns A:
# a = ord('A')
# print(a)

# Pattern 7
# 1
# 22
# 333
# 4444
# 55555
# n = int(input('Enter number'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

#Pattern 8
# 1
# 12
# 123
# 1234
# # 12345
# n = int(input('Enter number'))
# for i in range(1,n+2):
#     for j in range(1,i):
#         print(j,end='')
#     print()

# Pattern 9
# 11111
# 2222
# 333
# 44
# # 5
# n = int(input('Enter number'))
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         print((i),end='')
#     print()

#Pattern 10

# 12345
# 1234
# 123
# 12
# #
# n=int(input('Enter number'))
# for i in range(1,n+1):
#     for j in range(1,(n-i+2)):
#         print((j),end='')
#     print()

#

