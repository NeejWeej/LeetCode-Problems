class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = float('inf')
        best_sell = float('-inf')
        profit = 0
        for price in prices:
            if price < best_buy:
                best_buy = price
                best_sell = float('-inf')
            elif price > best_sell:
                profit = max(profit, price - best_buy)
                best_sell = price
        return profit
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > best:
        #         best = price - min_price
        # return best
                
        