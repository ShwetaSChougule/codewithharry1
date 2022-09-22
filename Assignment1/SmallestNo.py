l = [2,3,4,5,6,7,8,8]

# Approach1
# using reduce
# from functools import reduce
# s = reduce(lambda a,b:a if a<b else b, l)
# print(s)

# Approach2
# l.sort()
# print('Smallest element is',l[0])
# n = len(l)

# Approach3
# print('Smallest element is',min(l))

#Approach4
# n = len(l)
# min = l[0]
# for i in range(n):
#     if l[i]<min:
#         min = l[i]
#
# print(min)


# print(s)