def twoSum(nums, target):
        
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]

#Try 1 - too slow (5696 ms) and takes up too much memory (13.6 MB)
       
        # for x in range(len(nums)):
        #     for y in range(len(nums)):
        #         if nums[x] + nums[y] == target:
        #             if x == y:
        #                 continue
        #             else:
        #                 return [x, y] 

#Try 2 - much faster (40ms) but slightly more memory (14.2 MB)

    numsDict = {}
    for x in range(len(nums)):
            numsDict[nums[x]] = x
            print (numsDict)

    for x in range(len(nums)):
        complement = target - nums[x]
        if numsDict.get(complement) and numsDict.get(complement) != x:
            return [x, numsDict.get(complement)]

#Testing
numbers = [3, 2, 3]
targetValue = 6
print(twoSum(numbers, targetValue))