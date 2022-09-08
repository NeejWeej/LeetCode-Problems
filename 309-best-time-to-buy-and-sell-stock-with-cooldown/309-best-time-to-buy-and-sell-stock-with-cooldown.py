class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        bestBuy = lastBuy = -prices[0]
        lastSell = float('-inf')
        lastCoolDown = 0
        
        for p in prices:
            cd = max(bestBuy, lastSell, lastCoolDown)
            buy = lastCoolDown - p
            sell = bestBuy + p
            bestBuy = max(buy, bestBuy)
            lastBuy, lastCoolDown, lastSell = buy, cd, sell
        
        return max(lastSell, lastCoolDown)
                
            