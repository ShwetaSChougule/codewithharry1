# # #Functions: function is a block of code which only runs when it is called.
# # def fun():
# #     """Function example"""
# #     print('Hello, this is function')
# #
# # fun()
# # # user defined or built in
#
# # prime
# flag = False
# num = int(input('Enter a number'))
# if num>1:
#     for i in range(2,num):
#         if (num%i) == 0:
#             flag = True
#             break
#         else:
#             # print('Number is prime')
#             flag = False
#
# if flag == True:
#     print('Number is not prime')
# else:
#     print('Number is prime')
#
#
# a = 517/11
# print(a)

# To check if number is prime:
n = int(input('Enter a number'))
flag = False

for i in (2,n):
    if (n%i)== 0:
        flag == True
        break
    else:
        flag == False

if flag == True:
    print('Number is prime')
else:
    print('Number is not prime')













