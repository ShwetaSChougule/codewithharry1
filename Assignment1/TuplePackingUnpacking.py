#Tuple packing and unpacking
a = ('yellow','orange','green') #packing
(Mango,Tangrine,grapes) = a
print(Mango)

b = ('One','Two','Three','Four')
(a,*b,c) = b
print(a)
print(*b)
