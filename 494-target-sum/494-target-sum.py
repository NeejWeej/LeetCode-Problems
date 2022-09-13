class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0
        n = len(nums)
        dp = {}
        
        def dfs(nums, idx, target):
            if (idx, target) in dp:
                return dp.get((idx, target))
            
            if idx == n:
                if target == 0:
                    dp[(idx, target)] = 1
                    return 1
                else:
                    dp[(idx, target)] = 0
                    return 0
                
            else:
                left = dfs(nums, idx + 1, target - nums[idx])
                right = dfs(nums, idx + 1, target + nums[idx])
                dp[(idx, target)] = left + right
                return left + right
        
        return dfs(nums, 0, target)
