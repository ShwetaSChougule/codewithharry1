# import re
# a = re.compile('Shw')
# print(type(a))

# import re
# obj =re.finditer("[abc]",'abgjkc')
# for i in obj:
#     print(i.start(),' ',i.group())
# match -- searches from beggining- difference between match and search
import re
a = 'ab'
m = re.match(a,'abc')
print(m)

# findall
import re
# a = 'ab'
m = re.findall("[abc]",'abc')
print(m)

# search
import re
a = 'ab'
m = re.search(a,'abc')
print(m)

# sub- substitution
# subn- how many times replacement occurs
import re
m = re.sub('[A-Z]','*','zCUer')
print(m)

import re
m = re.subn('[A-Z]','*','zCUer')
print(m)


# split
import re
m= re.split(',','Shweta,Chougule,Sangli')
print(m)

# fullmatch
import re
a = 'auyhbss65'
m = re.fullmatch(a,'auyhbss65')
print(m)
