class Solution:
    from itertools import islice
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        last2 = 0
        for idx, num in enumerate(islice(nums, 1, n - 1), 1):
            dp[idx] = max(num + last2, dp[idx - 1])
            last2 = dp[idx - 1]
        bestWith = dp[-2]
        dp[0] = nums[1]
        last2 = 0
        for idx, num in enumerate(islice(nums, 2, n), 2):
            dp[idx - 1] = max(num + last2, dp[idx - 2])
            last2 = dp[idx - 2]
        return max(bestWith, dp[-2])
            