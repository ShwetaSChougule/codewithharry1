l = [2,3,4,5,6,7,8,8]
# Approach1
# n = len(l)
# b = l[0]
# for i in range(n):
#     if l[i]>b:
#         b = l[i]
# print(b)

# Approach2
# print(max(l))

# Approach3
# a = sorted(l,reverse=True)
# print(a[0])

# Approach4
from functools import reduce
b = reduce(lambda a,b:a if a>b else b,l)
print(b)





