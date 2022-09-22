a = [3,4,5,6,7,8,9]
# array multi divided by n
n = len(a)
print(n)
mul = 1
for i in range(n):
    mul = mul * a[i]

print(mul)
if mul != 0:
    r = mul%n
print(r)






