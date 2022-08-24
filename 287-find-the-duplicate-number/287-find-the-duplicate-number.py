class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = float('inf')
        for idx, val in enumerate(nums):
            absVal = abs(val)
            if nums[absVal - 1] < 0:
                ans = absVal
                break
            nums[absVal - 1] *= -1
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return ans
            
        # n = len(nums) - 1
        # return sum(nums) - (n*(n+1))//2