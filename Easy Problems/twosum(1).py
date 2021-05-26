#Solution ran in 32 ms and use 13.5 MB of storage

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0, len(nums)):
        for j in range((i + 1), len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#Testing
numbers = [3, 2, 3]
targetValue = 6
print(twoSum(numbers, targetValue))