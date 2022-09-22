def swap(l,a,b):
    first = l.pop(a-1)
    second = l.pop(b-2)

    l.insert(a,second)
    l.insert(b,first)

    return list
list = ['a','b','c','d','e']    #b e
# ['a','e','c','d','b']
p1 = 2
p2 = 5
print(swap(list,p1,p2))
# f = l.pop(1)
# f = l.pop(3)
#
# l.insert(1,'e')
# l.insert(4,'b')
# print(l)