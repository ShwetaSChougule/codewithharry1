#interchange first and last element of array
a = [3,4,5,6,7,8]
# Approach1
n = len(a)
# a[0],a[n-1] = a[n-1],a[0]
# print(a)

# Approach2
temp = 0
temp = a[n-1]
a[n-1] = a[0]
a[0] = temp
print(a)
