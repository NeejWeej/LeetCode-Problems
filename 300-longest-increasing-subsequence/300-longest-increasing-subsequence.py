class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = best = 1
        
        for idx, num in enumerate(nums[1:], 1):
            # longest one ending with current index
            dp[idx] = 1
            for i in range(idx):
                if nums[i] < num and dp[idx] < dp[i] + 1:
                    dp[idx] = dp[i] + 1
                    best = max(dp[idx], best)
        return best