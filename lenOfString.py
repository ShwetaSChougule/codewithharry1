import functools
str = 'hi there'
# # 1
# l = len(str)
# print(l)
#
# # 2
# c = 0
# for i in str:
#     c+=1
#
# print(c)

# 3
# c= 0
# i= 0
# while str[c:]:
#     i = i+1
# print(i)
# z = functools.reduce(lambda x:x+1,str,0) #reduce(function,sequence,initial)
# print(z)

tup = (2,1,0,2,2,0,0,2)
print(functools.reduce(lambda x, y: x+y, tup,6))