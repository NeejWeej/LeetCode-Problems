class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for spot in range(len(dp)):
                if dp[spot] > 0 and spot + coin < len(dp):
                    dp[spot + coin] += dp[spot]
        return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # coins.sort()
        # n_coins = len(coins)
        # ways_to_make = [0 for i in range(amount+1)]
        # ways_to_make[0] = 1
        # for coin in coins:
        #     for j in range(coin, amount +1):
        #         ways_to_make[j] += ways_to_make[j-coin]
        # return ways_to_make[amount]