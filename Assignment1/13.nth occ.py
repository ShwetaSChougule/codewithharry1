l = ['Python', 'brainworks','Narhe','Python']
n = 'brainworks'
o,a= 1,0
a=0
count = 0
for i in l:
    a+=1
    if i == n:
        count+=1
        if count == o:
            print(a)