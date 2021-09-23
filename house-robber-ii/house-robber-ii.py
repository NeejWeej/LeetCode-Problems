class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) - 1)
        dp[0] = nums[0]
        for i in range(1, len(nums) - 1):
            SecondToLast = 0
            if i > 1:
                SecondToLast = dp[i-2]
            dp[i] = max(dp[i-1], SecondToLast + nums[i])
        incStart = dp[-1]
        dp[0] = nums[1]
        for i in range(1, len(nums) - 1):
            SecondToLast = 0
            if i > 1:
                SecondToLast = dp[i - 2]
            dp[i] = max(dp[i-1], SecondToLast + nums[i + 1])  
        return max(incStart, dp[-1])
        
            