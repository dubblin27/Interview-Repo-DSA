# #amazon(most asked),apple 

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:

#     All inputs will be in lowercase.
#     The order of your output does not matter.


# Link : https://leetcode.com/problems/group-anagrams/

# def sortedd(arr1):
#     arrx = []
#     for items in arr1 :
#         items[0] = ''.join(sorted(items[0]))
#         arrx.append(items[0])
#     return arrx

def sortedd(arr1) :
    arr_x = []
    for i in range(0,len(arr1)) :
        arr_x.append([''.join(sorted(arr1[i][0])), i])
    return arr_x

def main_append(ori,sor) :
    for i in range(len(sor)):
        # if sor[i][0] not in  :
        if sor[i][0] not in found    
        








arr = ["eat", "tea", "tan", "ate", "nat", "bat"] 
arr1 = []
for i in range(0,len(arr)):
    z = []
    z.append(arr[i])
    z.append(i)
    arr1.append(z)
arr3 = arr1 
# print(arr1)
arr2 = sortedd(arr1)
print(arr1)
print(arr2)
# print(arr1)
main_append(arr1,arr2)




# def sortedd(arr):
#     main_dict = {}
#     for i in range(0,len(arr)):
#         # print(arr[i])
#         print(main_dict)
#         arr[i] = ''.join(sorted(arr[i]))  
#         print(arr[i])
#         main_dict[arr[i]] = i
#     print(main_dict)

# arr = ["eat", "tea", "tan", "ate", "nat", "bat"] 
# dict = {}
# for i in range(0,len(arr)):
#     dict.__setitem__(arr[i],i)
# print(dict)

# main_arr = sortedd(arr)
# print(main_arr)
# # main arr = []

# # for items in arr :
