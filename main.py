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