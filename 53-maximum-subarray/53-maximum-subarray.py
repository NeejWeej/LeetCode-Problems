class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = float('-inf')
        for idx, num in enumerate(nums):
            cur = max(cur + num, num)
            best = max(best, cur)
        return best
        