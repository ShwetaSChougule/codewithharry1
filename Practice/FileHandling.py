test_list = ['a','ab','abc','abcd']
res = []
test_list.sort(key = len)
print(test_list)

print(len)
for idx,val in enumerate(test_list):
    if val not in ', '.join(test_list[idx+1:]):
        res.append(val)

print(res)


