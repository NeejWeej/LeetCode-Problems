class Solution:
    from itertools import islice
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        dp = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            bestBuy = prices[i]
            bestVal = 0
            for j in range(i + 1, n):
                if prices[j] < bestBuy:
                    bestBuy = prices[j]
                else:
                    nextStart = dp[j + 2] if j + 2 < n else 0
                    bestVal = max(bestVal, prices[j] - bestBuy + nextStart)
            dp[i] = bestVal
        return dp[0]
                
            