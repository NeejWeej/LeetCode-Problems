class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        best_price_to_buy = float('inf')
        for price in prices:
            money_we_can_make = price - best_price_to_buy
            if money_we_can_make > best_profit:
                best_profit = money_we_can_make
            if price < best_price_to_buy:
                best_price_to_buy = price
        
        return best_profit
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = 0
        # min_price = float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > best:
        #         best = price - min_price
        # return best
                
        