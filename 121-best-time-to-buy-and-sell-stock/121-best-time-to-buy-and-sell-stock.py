class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        max_profit = 0
        for idx in range(1, len(prices)):
            cur_val = prices[idx]
            max_profit = max(max_profit, cur_val - best_buy)
            best_buy = min(best_buy, cur_val)
        return max_profit
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > best:
        #         best = price - min_price
        # return best
                
        