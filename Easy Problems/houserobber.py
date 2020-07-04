def rob(nums):
    #:type nums: List[int]
    #:rtype: int
    
# Try 1 - does not work for all cases

    # if len(nums) == 0:
    #     return 0

    # evens = 0
    # odds = 0

    # for i, num in enumerate(nums):
    #     if i % 2 == 0:
    #         evens += num
    #     else:
    #         odds += num

    # ends = 0
    # if len(nums) > 2:
    #     ends += nums[0]
    #     ends += nums[len(nums) - 1]
    
    # if evens > odds and evens > ends:
    #     return evens
    # elif ends > odds:
    #     return ends
    # else:
    #     return odds

# Try 2 - (copied from a solution found on leetcode) ran in 24 ms and used 12.6 MB of memory

    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    rob1, rob2 = 0, 0
        
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

#Testing
nums = [1, 3, 1, 3, 100]
print(rob(nums))