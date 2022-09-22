# # l4 = ['a','b','c','d','e','f','g','h','i','j']
# # print(l4[1:3:2])
#
# l4 = ['a','b','c','d','e','f','g','h','i','j']
# l5 = ['h']
# print(l4[-8:-3])
# print(l4[:])
# print(l4[::-1])
# print(l4[2:7:2])
#
# # add methods: replace,insert,append,extend
# l4[0] = 's'
# print(l4)
#
# l4.insert(1,'p')
# print(l4)
#
# l4.append('l')
# print(l4)
#
# l4.extend(l5)
# print(l4)
#
# #remove,pop,del, clear
#
# l4.remove('h')
# l4.pop()
# l4.pop(2)
# del l4[0:6]
# l4.clear()
# print(l4)

# splitting the array and putting to last:
l = [1,2,3,4,5,6]
le = len(l)

n = int(input("Enter a number"))

print(l[0:n])
print(l[n:le])