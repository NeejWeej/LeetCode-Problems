class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        best = float('-inf')
        cur = 0
        for num in nums:
            cur += num
            if cur > best:
                best = cur
            if cur < 0:
                cur = 0
        return best
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #O(n) space
        #O(n) time
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(nums[i] + dp[i-1], nums[i])
        # return max(dp)
        #-------------------------------------------------
        #O(1) space
        #O(n) time
        # best, curr = nums[0], 0
        # for val in nums:
        #     curr = max(val, curr + val)
        #     best = max(best,curr)
        # return best
            
            
                
        
        
        
        
        