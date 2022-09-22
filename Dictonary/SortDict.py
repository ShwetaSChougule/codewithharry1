d = {78:'a',2:'s',3:'c'}
# dict can be sorted by using sorted function
k = sorted(d.keys())
print(k)
v = sorted(d.values())
print(v)

i = sorted(d.items())
print(i)

# n= input('enter keyvalue pair')
d= {}
n = int(input('Enter number'))
for i in range(n):
     k = input('enter key')
     v = input('Enter value')
     d.update({k:v})
print(d)






