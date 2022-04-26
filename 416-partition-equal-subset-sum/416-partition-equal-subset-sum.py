class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1: return False
        target = total // 2
        dp = [set() for _ in range(n)]
        dp[-1].add(nums[-1])
        dp[-1].add(0)
        for i in range(n - 2, -1, -1):
            cur = nums[i]
            for num in dp[i + 1]:
                if num + cur <= target:
                    dp[i].add(num + cur)
                    dp[i].add(num)
                elif num <= target:
                    dp[i].add(num)
        return target in dp[0]
                
            