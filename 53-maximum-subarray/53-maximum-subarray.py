class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = float('-inf')
        curStart = -1
        bestS, bestE = -1, -1
        for idx, num in enumerate(nums):
            if cur + num < num:
                curStart = idx
                cur = num
            else:
                cur += num
            if best < cur:
                bestS = curStart
                bestE = idx
                best = cur
        print(nums[bestS: bestE + 1])
        return best
        