class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, best = 0, float('inf')
        for price in prices:
            profit, best = max(profit, price - best), min(price, best)
        return profit