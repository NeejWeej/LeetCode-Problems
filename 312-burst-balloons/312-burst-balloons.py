class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = nums[0] * nums[1]
        dp[-1][-1] = nums[-1] * nums[-2]
        for i in range(1, n - 1):
            dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]

        
        for e in range(n):
            for s in range(e - 1, -1, -1):
                
                for popLast in range(s, e + 1):
                    left = right = 0
                    if popLast > s:
                        left = dp[popLast - 1][s]
                        
                    if popLast < e:
                        right = dp[e][popLast + 1]
                    
                    mid = nums[popLast]
                    mid *= nums[s - 1] if s > 0 else 1
                    mid *= nums[e + 1] if e < n - 1 else 1
                    dp[e][s] = max(dp[e][s], left + mid + right)          
        return dp[n-1][0]
                    
                
                
        
                
                