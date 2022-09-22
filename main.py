# # list
#
# list1 = [23,34,5,657,8,9,9,9,678]
# # sort, reverse,copy,append, insert,del,clear,remove,pop,list constructor
#
# list1.sort()
# print(list1)
#
# list1.reverse()
# print(list1)
#
# list2 = []
# list2 = list1.copy()
# print(list2)
#
# list1.append("Shweta")
# print(list1)
#
# list1.insert(0,"56")
# print(list1)
#  # remove particular item
# list1.remove(657)
# print(list1)
#
# # pop
# list1.pop()
# print(list1)
#
# list2.pop(4)
# print(list2)
#
# del list2[0:5]
# print(list2)
#
# del list2
#
# list1.clear()
# print(list1)
#
# list3 = ((56,8,6,8,4))
# print(list3)
#
# # removing all the empty lists:
#
# list4 =  [67,4,45,6,7,[],333,[],[]]
# list5= []
# for x in list4:
#     if x != []:
#         list5.append(x)
#
# print(list5)
#
#
list6 = [56,4,8,6,8,[67,23],78,[90,80,67],[]]
print(type(list6))
# print(len(list6))

x=0
summ =0
a = 0
for x in list6:
    if type(x) == list:
        a = len(x)
        summ = summ + a
    else:
        a == 1
        summ = summ + a
print(summ)


# Count unique items in a list, convert it to set
list7 = [3,3,3,4,5,7,8,8,9]
set2 = set(list7)
print(len(set2))

# To get duplicate items in a kist

dup = []
print(list7)
for i in list7:
    if list7.count(i) > 1:
        if i not in dup:
            dup.append(i)

print(dup)

# To find the occurrence in a list
from collections import Counter

mylist = ["a","b","c","d","a","e","w","w","f","t","t"]

duplicate_list = Counter(mylist)
print(duplicate_list)

# Number of non zero elements.

list_x = [80,0,78,56,9,78,0,8,0,6,0,5,0,0,9]
list_y = []
for i in list_x:
    if i != 0:
        list_y.append(i)

print(list_y)

#Finding total number of elements in a nested lists
list_u = [[67,23],[90,80,67],[]]
print(sum(map(len,list_u)))


range(15)
print(list(range(20)))

import random
print(random.randrange(0,20))

import random
random.randrange(0,10)

# multiline string
print("""Hi This is Shweta
I  am a python developer""")

for x in "banana":
    print(x,"\n")

a = "    Hey,this is Shweta"
print(a.strip())
print(a.replace("H","Y"))
print(a.split(","))

# Not possible.
age = 30
txt = "Hi, my age is {}"
# summ = txt + age
# print(txt)

# but
print(txt.format(age))
