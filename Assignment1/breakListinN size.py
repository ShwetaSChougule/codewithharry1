l = [1,2,3,4,5,6,7,8,9]

# for i in range(0,len(l),2):
#     print(l[i:i+2])


# using yield:
# def gen(l,n):
#     for i in range(0,len(l),n):
#         yield l[i:i+n]
#
# a = list(gen(l,3))
# print(a)


# # example using iter method:
#
# value = 'geeks'
# obj = iter(value)
#
# while  True:
#     try:
#         item = next(obj)
#         print(item)
#     except StopIteration:
#         break
#
#
# # range:
# for i in range(0,4,2):
#     print(i)
#
