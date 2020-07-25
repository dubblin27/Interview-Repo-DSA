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

def groupana(arr):
    result = []
    mymap = {}
    count = 0 
    for idx, word in enumerate(arr):
        # print(idx,word)
        key = sorted(word)
        key = ''.join(key)

        if key in mymap:
            (result[mymap[key]]).append(word)
            (result[mymap[key]]).sort()
            print(result[mymap[key]])
        else :
            anagram = [word]
            result.insert(idx,anagram)
            mymap[key] = count;
            count +=1 
    result.sort(key = len)
    return result
arr = ["eat","tea","tan","ate","nat","bat"] 

print(groupana(arr))


# -----------------------

# Leet soln 1 :

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        myMap = {}
        count = 0
        for idx, word in enumerate(strs):
            key = sorted(word)
            key = ''.join(key)
            if key in myMap:
                (result[myMap[key]]).append(word)
                result[myMap[key]].sort()
                
            else:
                anagram = [word]
                result.insert(idx, anagram)
                myMap[key] = count;
                count += 1
                
        result.sort(key=len)
        return result

# Leet soln 2 :
from functools import reduce
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def f(acc, s):
            key = ''.join(sorted(s))
            if key in acc:
                acc[key] += [s]
            else:
                acc[key] = [s]
            return acc

        return reduce(f, strs, {}).values()