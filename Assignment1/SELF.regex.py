#match= to check if the given string is at start of target string

import re

# s = input('Enter pattern to check')

# m = re.match(s,'abc')
# if m!= None:
#     print('Match available')
#     print('At',m.start(),'end at',m.end())
# else:
#     print('No match')

#fullmatch
# m = re.fullmatch(s,'shweta')
# if m!= None:
#     print('Match found')
# else:
#     print('no match')

# m = re.finditer('009','009567009')
# for i in m:
#     print(i.start(),i.end())
#
#
# # sub
# m = re.sub('sa','hi','saghsa')
# print(m)
#
# binary string
s = input('Enter string')
m = re.search('[0-1]',s)
if m!= None:
    print('yes')
else:
    print('no')



