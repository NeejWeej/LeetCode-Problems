class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0]+nums[2],nums[1])
        best = [0]*n
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])
        for idx, val in enumerate(nums[1:],1):
            best[idx] = max(val + best[idx-2],best[idx-1])
        return best[-1]
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0],nums[1])
        # if n == 3:
        #     return max(nums[0]+nums[2],nums[1])
        # return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))