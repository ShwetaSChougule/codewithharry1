# #By placing sequence inside [ ]:
# mutable, ordered,indexed,allows dupes,
# List = []
# print(List)
#
# # List Constructor
# # syntax : list(iterable)
#
# text = 'Python'  #String
# l1 = list(text)
#
# print(l1)
# tup = ('P','y','t','h','o','n')
# l2 = list(tup)
# print(l2)
#
# dict =  {1:'a',2:'b'}
# l3  = list(dict)
# print(l3)
#
# # Accessing list elements and slicing:
#
l4 = ['a','b','c','d','e','f','g','h','i','j']
#      0   1   2   3   4   5   6   7   8   9     # Positive indexing
#    -10  -9  -8  -7  -6  -5  -4  -3  -2  -1     # Negative indexing
#
# print(l4[0])
# print(l4[-1])

# print(l4[:])
# print(l4[0:])
# print(l4[:7])
# print(l4[0:5])
# print(l4[2:7])                                   #Range of indexes
# print(l4[2:-3])
# print(l4[-8:7])
# print(l4[-8:-3])
# print(l4[::-1])
# print(l4[1::2])                  #start:end:step
#
# Change Values
l5 = ['India','Japan','Singapore','Belgium','China','Korea']
# l5[3] = 'Finland'  "gets replaced
# print(l5)
#
# Changing range of items:
# l5[2:5] = ['Indonesia']
# print(l5)
# this will produce l5 as, ['India','Japan','Indonesia']
# but l5[2:5] = 'Indonesia' will create as,
# ['India', 'Japan', 'I', 'n', 'd', 'o', 'n', 'e', 's', 'i', 'a', 'Korea']
#
# # ADDING LIST ITEMS
# # Item insertion
# l5.insert(2,'Greece')
# print(l5)
#
# # Appending Items:
# l5.append('Thailand')
# print(l5)

#
# Extend list
# list1 = ['Nagpur','Mumbai','Delhi','Dehradun','Rishikesh']
# list2 = ['Banglore','Pune','Shimla']
# Tup = ('Mangalore','Ooty','Munnar')
# Dic = {'Hyderabad':34,'Chennai':30}
# list1.extend(list2)
# list1.extend(Tup)
# list1.extend(Dic)
# print(list1)

# # REMOVING LIST ITEM
# list1.remove('Nagpur')
# print(list1)
#
# print(list2)
# list2.pop(0)
#
# list2.pop()
# print(list2)
#
# del list1[0]
# print(list1)
#
# # To delete entire list
# del list2
# # print(list2)
#
# list1.clear()
# print(list1)
#
# # Looping a list
# # list1 = ['Nagpur','Mumbai','Delhi','Dehradun','Rishikesh']
# # for i in list1:
# #     print(i)

# # # loop using index:
# list2 = ['Banglore','Pune','Shimla']
# for i in range(len(list2)):
#      print(list2[i])

# # while loop
# list2 = ['Banglore','Pune','Shimla']
# i = 0
# n  = len(list2)
# print(n)
# while i < n:
#     print(list2[i])
#     i+=1

# splitting array and adding to last
l = [2,3,4,5,6,7]
t = len(l)
n = int(input('Enter no'))
l = l[n:t] + l[0:n]
print(l)






