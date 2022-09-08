class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        bestBuy = -prices[0]
        lastSell = float('-inf')
        lastCoolDown = 0
        
        for p in prices:
            cd = max(bestBuy, lastSell, lastCoolDown)
            sell = bestBuy + p
            bestBuy = max(lastCoolDown - p, bestBuy)
            lastCoolDown, lastSell = cd, sell
        
        return max(lastSell, lastCoolDown)
                
            