class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for val in range(1, amount+1):
            min_num = float('inf')
            for coin in coins:
                if val - coin >= 0 and dp[val-coin] != -1:
                    min_num = min(min_num, 1 + dp[val-coin])
            if min_num == float('inf'):
                min_num = -1
            dp[val] = min_num
        return dp[-1]
                    
                    
            
            
        
