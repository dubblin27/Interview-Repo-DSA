
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

# Example:

# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
def freq(arr) :
    unique_words = set(arr)
    dict = {}
    for words in unique_words :
        dict.__setitem__(words,arr.count(words))
    return dict
def convert(lst): 
    return ' '.join(lst).split() 

lst =  "a, a, a, a, b,b,b,c, c"
lst.replace(",", " ")  
        

print(lst)
banned = ["a"]


lst = lst.lower()
for items in lst :
    items = ''.join(e for e in items if e.isalnum())
lst = [lst]

lst =  convert(lst)
# print(lst)
# banned = ["hit"] 
for items in lst :
    if items in banned :
        lst.remove(items)


dict = freq(lst)
print(dict)
a = 0
for i in dict.values() :
    if i >= a :
        a = i 
# print(list(dict.keys()))[list(dict.values()).index(a)]
