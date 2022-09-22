# s = 'SHWETA'
# l = s.lower()
# print(l)
#
# u = l.upper()
# print(u)
#
# # String methods
# # capitalize - to make capital first letter.
# # syntax - string.capitalize()
# str = 'python'
# print(str.capitalize())
#
# # If we have to make first letter of each word capital, use title()
# # syntax: string.title()
# str1 = 'We are python developers'
# print(str1.title())

# Casefold -

# To check if string is palindrome
str = 'geeksforGeeks'
str = str.casefold()
print(str)

rev_str = ''.join(reversed(str))
print(rev_str)

if str == rev_str:
    print('Strings are palindrome')
else:
    print('Strings are not palindrome')




