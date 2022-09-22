#json to python  :dump.
import json
x = {"a":2,"b":3,"c":5 ,"d":6 }   #dict file
print('Dict be like',x)
print(type(x))
y = json.dumps(x)
print(y)
print(type(y))

# converting json to dict
z = json.loads(y)
print(z)
print(type(z))