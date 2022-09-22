a = ['a','z','r','t','y']
# a, d = 2,n = length of array
def rotation(arr,d,n):
    arr[:] =  arr[d:n] + arr[0:d]
    print(arr[:])

rotation(a,2,len(a))

b = len(a)
if b%2 == 0:
    h = b/2
    rotation(a,h,b)
else:
    print('error')