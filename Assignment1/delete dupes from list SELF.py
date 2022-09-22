l = [2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5]
#1
res = []
for i in l:
    if i not in l:
        res.append(i)
print(res)

# list comprehension
[res.append(i) for i in l if i not in res]
print(res)

# using set : but not ordered
s = set(l)
print(s)






