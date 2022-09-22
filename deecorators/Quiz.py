import time
c =0
a = input('Welcome to Quiz,are you ready?')
if a != 'yes':
    print('Ok,bye')
    quit()

time.sleep(2)
#q1
print('1.Which State has largest area?')
time.sleep(2)
print('A.Maharashtra')
time.sleep(1)
print('B.Madhya Pradesh')
time.sleep(1)
print('C.Uttar Pradesh')
time.sleep(1)
print('D.Rajasthan')
ans = input()

if ans =='D':
    print('Yes! right answer')
    c+=1
else:
    print('Better luck next time! \U0001F643')

# q2
time.sleep(1)
print('2.In what state is Elephant Falls located')
time.sleep(2)
print('A.Mizoram')
time.sleep(1)
print('B.Orissa')
time.sleep(1)
print('C.Manipur')
time.sleep(1)
print('D.Meghalaya')
ans = input()

if ans =='D':
    print('Yes! right answer')
    c+=1
else:
    print('Better luck next time! \U0001F643')

# q3
time.sleep(1)
print('3.Which is the largest coffee-producing state of India')
time.sleep(2)
print('A.Kerala')
time.sleep(1)
print('B.Tamil Nadu')
time.sleep(1)
print('C.Karnataka')
time.sleep(1)
print('D.Meghalaya')
ans = input()

if ans =='C':
    print('Yes! right answer')
    c+=1
else:
    print('Better luck next time! \U0001F643')

# q4
time.sleep(1)
print('3.How many states are there in India')
time.sleep(2)
print('A.20')
time.sleep(1)
print('B.28')
time.sleep(1)
print('C.29')
time.sleep(1)
print('D.25')
ans = input()

if ans =='B':
    print('Yes! right answer')
    c+=1
else:
    print('Better luck next time! \U0001F643')

# q5
time.sleep(1)
print('4.How many Union Territories are there in India')
time.sleep(2)
print('A.9')
time.sleep(1)
print('B.7')
time.sleep(1)
print('C.8')
time.sleep(1)
print('D.6')
ans = input()

if ans =='C':
    print('Yes! right answer')
    c+=1
else:
    print('Better luck next time! \U0001F643')

if c > 3:
    print('Great job! Keep it up')
else:
    print('oh no!you scored {} out of 5'.format(c))