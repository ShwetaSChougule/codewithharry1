#
# lo = [3,7,5,9,4]
# def maxx(lo):
#     max = lo[0]
#     for i in lo:
#         if i >max:
#             max = i
#
#     print(max)
# maxx(lo)

# Finding most frequent element in a list:
test = [2,4,56,8,8,5,4,2,4,5,4,5,44,4,4,4,4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
max = 0
res = test[0]
for i in test:
    freq = test.count(i)
    if freq > max:
        max = freq
        res = i
print(res)

# Max with key
# a = 'Hi'
# b = 'Hey'
# c = 'Hello'
#
# max_value = max(a,b,c,key=len)
# print(max_value)

# r = max(test,key=test.count)
# print(r)