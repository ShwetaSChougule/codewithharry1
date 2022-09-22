
# List Comprehension
# Could be used for new list creation from other iterables, ie. tuples,strings,lists.
#  [expression] which will executed for each element using for loop

l = []
for i in 'Python':
    l.append(i)
    print(l)
# newlist = [expression(element) for (element) in oldlist if condition]

l = [i for i in 'Python']
print(l)

# list creation using Tuple
t = (3,4,5,6,7)
li = [i for i in t if i>3 ]
print(li)

# Dif
# Difference between for loop and list comprehension in terms of time of exection.
# execution time for list creation is more for loop.
# But execution of functions is more in list com.

# Displaying table using list comprehension:
num = [i*10 for i in range(1,11)]
print(num)

num = [i*10 for i in range(1,11) if i%2==0]             #with condition
print(num)



