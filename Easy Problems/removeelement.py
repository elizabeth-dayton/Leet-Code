class Solution(object):
    def removeElement(self, nums, val):
        k = len(nums)
        try:
            while(True):
                nums.remove(val)
                k = k - 1
        except ValueError:
            return k
        
nums = [0,1,2,2,3,0,4,2]
val = 2
mysolution = Solution()
k = mysolution.removeElement(nums, val)
print(k)
print(nums)