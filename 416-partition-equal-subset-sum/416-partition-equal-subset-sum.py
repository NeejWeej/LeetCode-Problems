class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1: return False
        dp = [set() for _ in range(n)]
        dp[-1].add(nums[-1])
        dp[-1].add(-nums[-1])
        for i in range(n - 2, -1, -1):
            cur = nums[i]
            for num in dp[i + 1]:
                dp[i].add(num + cur)
                dp[i].add(num - cur)
        return 0 in dp[0]
                
            