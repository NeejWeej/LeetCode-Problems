class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * len(nums)
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            best = float('inf')
            jmp_size = nums[i]
            for j in range(i + 1, min(n, i + jmp_size + 1)):
                if dp[j] == -1:
                    continue
                best = min(best, 1 + dp[j])
            if best == float('inf'):
                dp[i] = -1
            else:
                dp[i] = best
        return dp[0]
        