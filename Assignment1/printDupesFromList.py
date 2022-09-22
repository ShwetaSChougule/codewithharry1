l = [3,4,5,6,4,5,64,6,3,8]
new = []
for i in l:
    n = l.count(i)
    if n >1:
        if new.count(i) == 0:
            new.append(i)

print(new[:])



