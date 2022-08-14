class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        buys = [float('inf') for _ in range(k)]
        sells = [0 for _ in range(k)]
        for p in prices:
            buys[0] = min(p, buys[0])
            sells[0] = max(sells[0], p - buys[0])
            for i in range(1, k):
                buys[i] = min(buys[i], p - sells[i - 1])
                sells[i] = max(sells[i], p - buys[i])
        return sells[-1]