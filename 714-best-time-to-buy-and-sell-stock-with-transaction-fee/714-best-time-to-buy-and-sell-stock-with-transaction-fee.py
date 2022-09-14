class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # return sum(i - j - fee for i,j in zip(prices[1:], prices[:-1]) if i -j - fee > 0)
        n = len(prices)
        if n < 2:
            return 0
        dp = [0]*n
        # we can combine transactions b1,s1 b2,s2 if s1 - b1 - fee + s2 - b2 - fee < s2 - b1 - fee
        # s1 - b2 - fee < 0
        
        lastSell = -1
        bestBuy = [float('inf') for _ in range(n)]
        profit = 0
        for i,p in enumerate(prices):
            oldProfit = profit
            if lastSell == -1:
                profit += p - bestBuy[i - 1] - fee
            else:
                profit += max(p - bestBuy[i - 1] - fee, p - prices[lastSell]) 
                          # -lastSell (:= prices[lastSell] - bestBuy[lastSell] - fee) + p - bestBuy[lastSell] - fee)
            if profit <= oldProfit:
                profit = oldProfit
                bestBuy[i] = min(p, bestBuy[i - 1])
            else:
                lastSell = i
                bestBuy[i] = p
        
        return profit
        
#         best = float('inf')
#         profit = 0
#         for p in prices:
#             print(profit, p, best)
#             if p > best + fee:
#                 profit += p - best - fee
#                 best = p
#             else:
#                 best = min(best, p )
#         return profit
            