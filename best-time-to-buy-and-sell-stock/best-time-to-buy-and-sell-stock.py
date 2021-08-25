class Solution:
    # def maxProfit_recurse(self,prices):
    #     if len(prices) == 1:
    #         return [prices[0],prices[0],0]
    #     prev_ans = self.maxProfit_recurse(prices[1:])
    #     print(prev_ans)
    #     if prev_ans[1] - prices[0] > prev_ans[-1]:
    #         return [prices[0],prev_ans[1],prev_ans[1] - prices[0]]
    #     return prev_ans
    
        # best = 0
        # minval = float('inf')
        # for idx, val in enumerate(prices):
        #     if val < minval:
        #         minval = val
        #     elif val-minval > best:
        #         best = val-minval
        # return best
    
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best:
                best = price - min_price
        return best
                
        