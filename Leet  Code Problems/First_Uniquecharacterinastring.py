#amazon
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.

# Link : https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:  
        for i,j in OrderedDict(Counter(s)).items():
            if j == 1 :
                return s.index(i)
        return -1