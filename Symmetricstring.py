#if string is symmetrical or palindrome


s = input("Enter a string")
# to check if its symmentric
ss = s.strip()
l = len(ss)
print(l)
if l%2 == 0:
    s1 = int(l/2)
    first_half = ss[:s1]
    sec_half = ss[s1:]
    print(first_half,sec_half)

else:
    s2 = int((l-1)/2)
    first_half = ss[:s2]
    sec_half = ss[s2+1:]
    print(first_half,sec_half)

if first_half == sec_half:
    print("String is symmetric")
else:
    print("String is not symmetric")