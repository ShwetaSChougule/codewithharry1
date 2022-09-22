# To check if word is palindrome.
# e.g:  radar
n = input('Enter a string')

n1 = n[::-1]
print(n1)

if n == n1:
    print('yes')
else:
    print('no')
