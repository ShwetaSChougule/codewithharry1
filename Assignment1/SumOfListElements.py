l = [2,2,3,3,3,4,4,4,7,6,7,9,9,7]
# s = sum(l)
# print(s)

from operator import add
sum = 0
for i in l:
    sum = add(i,0) + sum

print(sum)
