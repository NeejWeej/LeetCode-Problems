class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - best_buy)
            best_buy = min(best_buy, price)
        return profit
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > best:
        #         best = price - min_price
        # return best
                
        