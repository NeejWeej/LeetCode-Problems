class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        goal = tot // k
        n = len(nums)
        nums.sort(reverse=True)
        if tot % k != 0 or max(nums) > goal:
            return False
        
        dp = [0] * k
        
        def dfs(idx):
            if idx == n:
                return len(set(dp)) == 1
    
            val = nums[idx]
            
            for i, v in enumerate(dp):
                lastCheck = False
                if v == 0:
                    lastCheck = True
                
                dp[i] += val
                if val + v <= goal and dfs(idx + 1):
                    return True
                dp[i] -= val
                if lastCheck:
                    return False  
        return dfs(0)
    
        # target, m = divmod(sum(nums), k)
        # if m: return False
        # dp, n = [0]*k, len(nums)
        # nums.sort(reverse=True)
        # def dfs(i):
        #     if i == n:
        #         return len(set(dp)) == 1
        #     for j in range(k):
        #         dp[j] += nums[i]
        #         if dp[j] <= target and dfs(i+1):
        #             return True
        #         dp[j] -= nums[i]
        #         if not dp[j]: break
        #     return False
        # return nums[0] <= target and dfs(0)
