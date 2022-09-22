
# to contain all the vowels
v = ['a','e','i','o','u']
new = []
str = input('Enter a string')
for i in str:
    if i in v:
        new.append(i)

v = sorted(v)
new = sorted(new)
if v == new:
    print('String is valid')
else:
    print('Not valid')
