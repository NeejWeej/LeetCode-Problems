class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last_price_bought = float('inf')
        for price in prices:
            if price < last_price_bought:
                last_price_bought = price
            if price > last_price_bought:
                profit += (price - last_price_bought)
                last_price_bought = price
        return profit