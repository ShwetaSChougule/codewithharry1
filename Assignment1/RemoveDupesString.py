#remove all dupes from string

n = input('Enter a string')
new = set()
for i in n:
    if n.count(i) >1:
        new.add(i)

print(new)
