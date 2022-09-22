l = [10,20,30,40,50,60]
l1 = []
j = l[0]
for i in range(len(l)):
    if i ==0:
        l1.append(l[0])
    else:
        j = j + l[i]
        l1.append(j)
print(l1)


# list comp:
[l1.append(j) for j in j = j+l[i]]