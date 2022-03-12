class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_best = 0
        cur_best_price = prices[0]
        for idx in range(1, len(prices)):
            cur_price = prices[idx]
            cur_best = max(cur_best, cur_price - cur_best_price)
            cur_best_price = min(cur_best_price, cur_price)
        return cur_best
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > best:
        #         best = price - min_price
        # return best
                
        