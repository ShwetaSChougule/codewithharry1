l = ['shweta','s','shwet','eta']
n = []
for i in l:
    n.append(len(i))

print(n)
s = max(n)
print(s)
for i in l:
    if len(i) ==s:
        print('largest anagram is',i)