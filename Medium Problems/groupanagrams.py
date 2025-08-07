class Solution(object):
    def groupAnagrams(self, strs):
        returnList = []
        singleList = []
        anagram = True
        if len(strs) == 1:
            returnList.append(strs)
            return returnList
        else:
            i = 0
            j = 0
            while i < len(strs):
                singleList.append(strs[i])
                strs.pop(0)
                while j < len(strs):
                    if len(singleList[i]) != len(strs[j]):
                        j = j + 1
                    else:
                        for letter in singleList[i]:
                            if singleList[i].count(letter) == strs[j].count(letter):
                                continue
                            else:
                                j = j + 1
                                anagram = False
                                break
                        if anagram == True:
                            singleList.append(strs[j])
                            strs.pop(j)
                            j = 0
                    anagram = True
                j = 0
                returnList.append(singleList)
                singleList = []
        return returnList
        
strs = ["eat","tea","tan","ate","nat","bat"]
mySolution = Solution()
print(mySolution.groupAnagrams(strs))