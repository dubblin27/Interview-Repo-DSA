def make_dict(strs):
    dict = {}
    x = []
    for i in range(len(strs)):
        x.append(''.join(sorted(strs[i])))
    for i in range(len(strs)):
        dict.setdefault(x[i], []).append(strs[i])
    main_strs = []
    for i in dict.values():
        main_strs.append(i)
    main_strs.sort(key=len)
    return main_strs


        
strs = ["eat","tea","tan","ate","nat","bat"] 

print(make_dict(strs))