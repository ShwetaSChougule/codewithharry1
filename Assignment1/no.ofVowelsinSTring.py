# count number of vowels:
s = {'a','e','i','o','u'}
s1 = set()
c = 0
str = input('Enter string')
for i in str:
    if i in s:
        c+=1
        s.add(i)

print(c)
print(s)