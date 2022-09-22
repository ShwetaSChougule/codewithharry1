str1 = 'Race'
str2 = 'care'
str1 = str1.lower()
str2 = str2.lower()
s1 = sorted(str1)
s2 = sorted(str2)

if len(s1) == len(s2):
    if s1 == s2:
        print('Anagram')
    else:
        print('Not anagram')
