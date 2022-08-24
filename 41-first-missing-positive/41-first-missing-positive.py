class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or n < nums[i]:
                nums[i] = float('inf')
        
        for idx, val in enumerate(nums):
            absV = abs(val)
            if absV == float('inf'):
                continue
            nums[absV - 1] = -1*abs(nums[absV-1])
        
        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
            
        return n + 1
        
        