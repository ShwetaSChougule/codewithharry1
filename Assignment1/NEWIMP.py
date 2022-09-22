#TO CHECK IF ALL VOWELS AE IN STRING
s = set()
a = 'aeiou'
v = ['a','e','i','o','u']
z = [i for i in a if i in v]
for j in z:
    s.add(j)
    if len(s) == 5:
        print('yes')