class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        
#         def pfSum(pile, length):
#             res = [0]
#             for p in pile:
#                 res.append(res[-1])
#                 res[-1] += p
#             return res
        
#         dpPiles = [pfSum(p, k + 1) for p in piles]
        
#         dp = [dpPiles[0] + [float('-inf') for _ in range(len(dpPiles[0]), k + 1)]] + \
#         [[float('-inf') for _ in range(k + 1)] for _ in range(n)]
        
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        start = 0
        for idx, val in enumerate(piles[0]):
            if idx == len(dp[0]) - 1:
                break
            dp[0][idx + 1] = dp[0][idx] + val
        
        for i in range(1, n):
            pileSize = len(piles[i])
            
            for coins in range(k + 1):
                best = 0
                cur = 0
                for inPile in range(min(pileSize, coins + 1)):
                    # cur = dpPiles[i][inPile]
                    last = dp[i-1][coins-inPile]
                    best = max(best, last + cur)
                    cur += piles[i][inPile]
                    
                if pileSize < coins + 1:
                    last = dp[i-1][coins - inPile - 1]
                    best = max(best, last + cur) 
                    
                dp[i][coins] = best
                
        return max(dp[n-1][:k + 1])

                
                
                
            
            