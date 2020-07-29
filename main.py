lst =  "a, a, a, a, b,b,b,c, c" 
# lst = [lst] 
# for i in lst :
#     if i!= " " :
#         i.replace(i," ")
#     if i != "a-zA-Z"  :
#         i.replace(i," ")
# print(lst)
words = lst.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)