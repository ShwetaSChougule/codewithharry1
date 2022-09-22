# #Delete numbers which are even.
#
# l = [2,3,4,5,6,6,7,8,9,88]
# res = []
# # [res.append(i) for i in l if i%2==0 ]
# # print(res[:])
# res = [i for i in l if i%2==0 ]
# print(res)
#
# # remove l[1:4]
# del l[1:5]
# print(l)
#
k = list((map(int,input('Enter keys').split())))
v = list((map(int,input('Enter keys').split())))
d = dict.fromkeys(k,v)
print(d)


