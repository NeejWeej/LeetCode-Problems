class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        profit = 0
        for p in prices:
            if p < min_buy:
                min_buy = p
            else:
                profit += p - min_buy
                min_buy = p
        return profit
        