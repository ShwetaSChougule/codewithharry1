# Palindrome
s = 'Nayan'
sc = s.casefold()
print(sc)

rev = ''.join(reversed(sc))
print(rev)

if sc == rev:
    print('Palindrom')
else:
    print('Not palindrome')

# center - returns a string that is padded with specified char
# syntax - string.center(length,fillchar)
s = 'Shweta'
# new = s.center(20)
new = s.center(20,'_')
print(new)

# Count - returns number of occurances of substring in string
# syntax - string.count(substring,start = ,end = )
stri = 'Hi there'
print(stri.count('Hi'))

# encode- UTF(Unicode Transformation Format), 8 - 8 bit values are used in encoding.
# UFT-8 is an encoding format.
# In python strings are already in UFT-8 format.
# PENDING






