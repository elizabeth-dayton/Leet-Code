def longestCommonPrefix(strs):
    
    # :type strs: List[str]
    # :rtype: str

    # Try 1 - ran in 20 ms and took 13.1 MB of memory
    if len(strs) == 0:
        return ""
    prefix = strs[0] 

    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
        i += 1
    return prefix
        
#Testing
strs = ["c", "acc", "ccc"]
print(longestCommonPrefix(strs))

strs1 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs1))

strs2 = ["leets", "leetcode", "leet", "leeds"]
print(longestCommonPrefix(strs2))