n = list(map(int,input('Enter numbers').split()))
for i in n:
    if i < 0:
        print('negative')
    else:
        print('Positive')