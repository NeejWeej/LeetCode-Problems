class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp = [0]*(target + 1)
        # multiple = 0
        # while multiple <= target:
        #     dp[multiple] = 1
        #     multiple += nums[0]
        # for i in range(1, len(nums)):
        #     for j in range(nums[i], target + 1):
        #         dp[j] += dp[j - nums[i]]
        # return dp[-1][-1]
        dp = [0]*(target + 1)
        dp[0] = 1
        nums.sort()
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[-1]