#     *
#    * *
#   * * *
#  * * * *
# * * * * *


k = 0

for i in range(1,6):
    for space in range((5-i)):
        print(end=" ")

    while k!= (2*i-1):
        print("*",end="")
        k+=1

        k = 0
        print()


    for i in range(1,6):
        for space in range((5-i)):
            print(end=" ")

    while k!= (2*i-1):
        print("*",end="")

        k+=1
    k = 0
    print()
