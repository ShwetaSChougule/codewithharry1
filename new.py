s = 'Shweta'
a = ''
for i in s:
    a= i +a

print(a)




def summation(a,b):
    ans =a+b
    print(ans)

summation(3,4)



class A:
    name = 'Shweta'
    def __init__(self):
        pass
    def hi(self):
        print('HI',self.name)

a = A()
a.hi()




x = set()
print(type(x))



l2 = [3,6,2,9]
big = 0
for i in l2:
    if i>big:
        big = i

print(big)

l1 = ['a','b','as']
l2 = []
for i in l1:
    if 'a' in i:
        l2.append(i)
print(l2)



l1 = [2,3,5]
l2 = [4,5]
l1.extend(l2)
print(l1)


le = [2,3,5,56,6]




# s = input("Enter a string")
# w = ''
# for i in s:
#     w = i+w
#
# if w == s:
#     print('String is palindrome')
# else:
#     print('none')

# Factorial:
f =1
n = int(input('Enter a number'))
if n<0:
    print('Error')
elif n ==0:
    print('1')
else:
    for i in range(1,n+1):
        f = f*i
    print(f)

s = 'Harekrishna'
a = s.replace('krishna','rama')
print(a)

a = lambda x:x**2
print(a(9))

v = lambda a:a**2
print(v(2))


num = [2,3,4]
re = map(lambda x:x**2,num)     #map(lambda,iterator)
print(list(re))




