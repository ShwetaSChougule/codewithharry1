# approach1
from functools import reduce
l = [55,67,44,77,890,67876]
# large = reduce((lambda a,b:a if (a>b) else b),l)
# print(large)

# 2
n = 0
for i in l:
    if i > n:
        n = i
print(n)
