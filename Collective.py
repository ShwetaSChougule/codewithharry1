# # w  = ['a','b','c','d','e']
# # print(w[0])
# # print(len(w))
# #
# # #  0  1   2   3   4
# # # -5  -4 -3  -2  -1
# #
# # print(w[2:4])
# # print(w[-3:-1])
# # print(w[-4])
# # print(w[0:4:2+])
# #
# # print(w)
# import string
# g = list(string.ascii_lowercase)
# print(g)
#
# list2 = ['a','b','c','d','e']
# # print(list2)
# # print(list2[:])
# # print(list2[:5])
# print(list2[1:4])
# print(list2[-4:-1])
#
# print(g[::2])
#
# #

# for i in list1:
#     if i == []:
#         list1.remove(i)
#
# print(list1)

#
# list1 = [1,2,[],45,[],8,[],[],7]
# list2 = []
# for i in list1:
#     if i != []:
#         list2.append(i)
#
# print(list2)#
#
#list = ordered, mutable, accepts duplicates
# Tuples = ordered, immutable,  accept duplicates
# Sets = ordered, immutable, does not accept duplicates
#Dict = 
#
# # print(list2[-4:4])
# # print(list2[1:-1])
#
#
# # lygometry
#
# # Slicing
#
#
# list2 = [56,89,55,77,4]
# list2.sort()
# print(list2)
# list2.reverse()
# print(list2)
#
# print(len(list2))
# print(max(list2))
# print(min(list2))
# print(min(list2))
# list2.append(67)
# print(list2)
# list2.insert(5,44)
# print(list2)
# list2.remove(56)
# print(list2)
# list2.pop()
# print(list2)

# Slicing
list3 = [45,7,5,7,8,9,5,67,7]
print(list3[2:6])
print(list3[-7:6])
print(list3[2:-3])

# Advanced Slicing

print(list3[2:6:1])
print(list3[2:6:2])
print(list3[::-1])

import string
g = list(string.ascii_lowercase)
print(g)

l4 = ['a','b','c','d','e','f','g','h','i','j']
print(l4[2:7])
print(l4[-8:7])
print(l4[2:-3])
print(l4[-8:-3])

print(l4[2:])
# print(list2[0])\

# print(list2[:4])
# print(list2[2:])
# print(list2[2:4])
# print(list2[-3:4])
# print(list2[-3:-1])

# range
lr = [*range(3,20,1)]
print(lr)

rtt = [*range(2,20)]
print(rtt)


if 3 in rtt:
    print("Yes")
else:
    print("Nope")

rtt[5] = 789
print(rtt)














pr = [*range(0,20)]
print(pr)
pr[0] = 99
print(pr)

# list constructor

pr.insert(0,55)
print(pr)


a1 = [66,78,"Hello","there"]
del a1[1:2]
print(a1)



a1 = [34,56,78,87]
a2 = [45,67,66]
a3 = [44,55,6,7]
a4 = zip(a1,a2,a3)
print(a4)


# delete,pop, remove
# Removes element
t = [34,5,6,6,56,54,3]
t.remove(34)
print(t)

t.pop(0)
print(t)

t.pop()
print(t)

del t[2:3]
print(t)

x =[3,4,5,5,5,]
x.clear()
print(x)


del t
print(t)



