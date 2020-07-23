#FB, APPLE
#Link : https://leetcode.com/problems/valid-palindrome/description/ 

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

 

# Constraints:
#     s consists only of printable ASCII characters.

#main code
def checkpalindrome(s) :
    return s == s[::-1]
inp = input()
without_extras = list([val for val in inp if val.isalnum()])
final_string = "".join(without_extras)
string = final_string.lower()
print(string)
print(checkpalindrome(string))

# Leetcode soln :
class Solution:
    def isPalindrome(self, s: str) -> bool:
        without_extras = list([val for val in s if val.isalnum()])
        final_string = "".join(without_extras)
        string = final_string.lower()
        return string == string[::-1]



    
