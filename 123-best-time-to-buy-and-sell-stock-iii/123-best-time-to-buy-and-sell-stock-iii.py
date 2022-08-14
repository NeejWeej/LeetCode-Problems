class Solution:
    from itertools import islice
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        forwardDp = [0 for _ in range(n)]
        min_so_far = prices[0]
        for i,p in enumerate(islice(prices, 1, n), 1):
            forwardDp[i] = max(forwardDp[i - 1], p - min_so_far)
            min_so_far = min(p, min_so_far)
        
        backDp = [0 for _ in range(n)]
        best_sell = prices[-1]
        enum = enumerate(reversed(prices), 1)
        # skip first entry in enumerate WITHOUT copying to a new list
        next(enum)
        for i, p in enum:
            idx = n - i
            backDp[idx] = max(backDp[idx + 1], best_sell - p)
            best_sell = max(p, best_sell)
            
        profit = 0
        for i in range(n):
            profit = max(profit, forwardDp[i] + backDp[i])
        return profit