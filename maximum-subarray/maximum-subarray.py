class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        n = len(nums)
        best = curr = nums[0]
        for val in nums[1:]:
            if curr <= min(0, best):
                curr = 0
            curr += val
            if best < curr:
                best = curr
        return max(best, curr)
            
            
                
        
        
        
        
        