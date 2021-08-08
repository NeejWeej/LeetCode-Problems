class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        n = len(nums)
        if n == 1:
            return nums[0]
        best_ending = curr_sum = float('-inf')
        for idx, val in enumerate(nums):
            if curr_sum < 0:
                curr_sum = val
            else:
                curr_sum += val
            if curr_sum > best_ending:
                best_ending = curr_sum
        return best_ending
                
        
        
        
        
        