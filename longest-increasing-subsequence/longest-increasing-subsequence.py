class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        best = 1
        for idx, val in enumerate(nums[1:], 1):
            for j in range(idx):
                if val > nums[j]:
                    dp[idx] = max(1 + dp[j], dp[idx])
            best = max(best, dp[idx])
        return best
            
        