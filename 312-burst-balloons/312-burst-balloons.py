class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for e in range(n):
            for s in range(e, -1, -1):
                
                for popLast in range(s, e + 1):
                    left = right = 0
                    if popLast > s:
                        left = dp[s][popLast - 1]
                        
                    if popLast < e:
                        right = dp[popLast + 1][e]
                    
                    mid = nums[popLast]
                    mid *= nums[s - 1] if s > 0 else 1
                    mid *= nums[e + 1] if e < n - 1 else 1
                    dp[s][e] = max(dp[s][e], left + mid + right)          
        return dp[0][n-1]
                    
                
                
        
                
                