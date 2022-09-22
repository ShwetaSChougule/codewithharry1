#matching characters:

str1 = input('Enter first string')
str2 = input('Enter  second string')
str1 = str1.casefold()
str2 = str2.casefold()
c = 0
l = []
for i in str1:
    for j in str2:
        if i == j:
            if i not in l:
                l.append(i)
                c = c+1

print(c)
print(len(l))
