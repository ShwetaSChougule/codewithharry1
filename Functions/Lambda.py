
# 
# print(l2)
# sorted:
# u  = [3,5,3,2,7,9,5,3,0]
# c = sorted(u,reverse=True)
# print(c)
# l = [[2,3,4,5],[3,4,56,6],[4,5,6]]
# soretdl = lambda x:(sorted(x) for x in l)

# print(soretdl(l))

# u  = [3,5,3,2,7,9,5,3,0]
# final = list(filter(lambda x:(x%2==0) ,u))
# print(final)
#
# p = [45,67,8,99,23,5]
# ppl= list(filter(lambda x:x>18,p))
# print(ppl)











#
#
# a = [5,6,44,3,3,4,5,6,7,8,9,80]
# b = sorted(a)
# print(b)
#
# c = sorted(b,reverse=True)
# print(c)
#
#
# # filter with lambda fn: even odd
# q = [2,3,4,5,6,7,8,9]
# res = list(filter(lambda x:(x%2==0),q))
# print(res)
#
# # map with lambda
# w = [4,5,6,6]
# res2 = list(map(lambda x:x*2,w))
# print(res2)
#
#
# animals = ['dog','cat','parrot']
#
#
#
# # reduce:
# from functools import reduce
# v = [3,4,5,6,7,]
# maxno = reduce(lambda a,b:a if (a>b) else b,v)
# print(maxno)
#
# # to filter out vowels using filter function
# seq = ['w','r','r','y','e']
# def func(n):
#     a = ['a','e','i','o','u']
#     if n in a:
#         return True
#     else:
#         return False
#
# result = filter(func,seq)
# for i in result:
#     print(i)
#


# operator function and reduce:
#
# from functools import reduce
# from operator import add

# import functools
# import operator
# y = [4,7,8,3,0,7,9]
# res= functools.reduce(operator.add,y)
# print(res)

# my_list = [12, 65, 54, 39, 102,  339, 221, 50, 70]
#
# result = list(filter(lambda x:x%13==0,my_list))
# print(result)

#
# my_list = ["geeks", "geeg", "keek", "practice", "aa"]
# res = list(filter(lambda str: str == str[::-1],my_list))
# print(res)
