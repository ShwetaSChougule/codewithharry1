# d = {'a':1,'b':2,'c':3}
# # Access elements:
# print(d['a'])
# print(d.get('a'))
# print(d.keys())
# print(d.values())
# print(d.items())
# 
# # add, update
# d['d']=4
# print(d)
# 
# d.update({'e':6})
# print(d)
# 
# # remove:
# # pop: will delete specific item:
# d.pop('a')
# print(d)
# d.popitem()
# print(d)
# del d['b']
# print(d)
# 
# # loop
# for i in d:
#     print(i)
# for i in d:
#     print(d[i])
# for i in d.keys():
#     print(i)
# 
# 
# x = ('a','b','c')
# y = 0
# d = dict.fromkeys(x,y)
# print(d)