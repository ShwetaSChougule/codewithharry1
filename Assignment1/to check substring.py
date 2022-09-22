str = 'Hi I am shweta,Shweta is a good girl'
sub = 'shweta'
# 1
# a = str.find(sub)
# print(a)

# 2
if str.count(sub) >0:
    print('yes')
else:
    print('no')

# 3
try:
    a = str.index(sub)
    print(a)

except:
    print('No')
