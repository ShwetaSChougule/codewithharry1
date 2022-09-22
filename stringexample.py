s = input('Enter a string')
new_s = s.strip()
print('Total length is,',len(new_s))
for i in new_s:
    a = new_s.count(i)
    print(f"the count {i}={a}")