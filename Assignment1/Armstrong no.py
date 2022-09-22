# result = power(a,n) + power(b,n)
n = int(input('Enter a number'))
p = len(str(n))
s = 0
if n == 0:
    print('0')
else:
    n1 = n
    while n1 > 0:
        digit = n1%10
        s = s + digit ** p
        n1= n1//10

if n == s:
    print('yes')
else:
    print('no')



