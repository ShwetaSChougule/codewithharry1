print('Enter number range')
n1 = int(input('Enter start number'))
n2 = int(input('Enter end number'))
l = []
if n1<n2:
    for i in range(n1,n2):
        for j in range(2,i):
            if i%j == 0:
                break
            else:
                l.append(i)
print(l)
[res.append(i) for i in l if i not in l ]
print(res)
