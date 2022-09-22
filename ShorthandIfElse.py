#  a = int(input("Enter first number"))
#  b = int(input("Enter second number"))
# #
#  print("A is greater than B") if a>b else print("B is greater than A")

# rows = int(input("Enter number of rows"))
#
# for i in range(rows):
#     for j in range(i):
#         print("*", end="")
#     print("\n")


rows = int(input("Enter number of rows"))
for i in range(rows):
    for j in range(i):
        print(j+1,end="")
    print("\n")

