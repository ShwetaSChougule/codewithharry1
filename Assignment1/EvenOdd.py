# Approach1
# l = list(map(int,input('Enter elements of list seperated by space:').split()))
# print(l)
# for i in l:
#
#     if i%2 == 0:
#         print('Number is even')
#     else:
#         print('Number is Odd')

# in a range:
l = []
l2 = []
n1 = int(input('Enter start of range'))
n2 = int(input('Enter end of range'))
if n1<n2:
    for i in range(n1,n2+1):
        if i%2 == 0:
            l.append(i)
        else:
            l2.append(i)

print(l,l2)

