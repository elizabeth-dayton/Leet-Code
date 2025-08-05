class Solution(object):
    def majorityElement(self, nums):
        numDict = {}
        for num in nums:
            if numDict.get(num) == None:
                numDict.update({num : 1})
            else:
                existingCount = numDict.get(num)
                numDict.update({num : existingCount + 1})

        for key in numDict:
            if numDict.get(key) > len(nums)/2:
                return key        