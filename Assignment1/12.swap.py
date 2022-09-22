
# # def swap(arr,a,b):
# #     a = a-1
# #     b = b-1
# #     arr[a],arr[b] = arr[b],arr[a]
# #     print(arr)
# # swap(arr,2,3)
#
# # using pop
# def swappop(arr,pos1,pos2):
#     pos1 = pos1-1
#     pos2 = pos2-1
#     print(pos1,pos2)
#     first = arr.pop(pos1)
#     second = arr.pop(pos2)
#     print(first)
#     print(second)
#     arr.insert(pos1,second)
#     arr.insert(pos2,first)
#     return arr
# a = [3,4,5,6,7]
# print(a)
# print(swappop(a,1,3))


# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)
    print(first_ele,second_ele)
    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


# Driver function
List = [23, 65, 19, 90]
# print(List)
# print(List[1])
# print(List[3])
pos1, pos2 = 2, 3

print(swapPositions(List, pos1, pos2))
