class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        def pfSum(pile, length):
            res = [0]
            for p in pile:
                res.append(res[-1])
                res[-1] += p
            return res
        
        dpPiles = [pfSum(p, k + 1) for p in piles]
        
        dp = [dpPiles[0] + [float('-inf') for _ in range(len(dpPiles[0]), k + 1)]] + \
        [[float('-inf') for _ in range(k + 1)] for _ in range(n)]
        
        for i in range(1, n):
            pileSize = len(dpPiles[i])
            
            for coins in range(k + 1):
                best = 0
                prevSize = len(dpPiles[i-1])
                
                for inPile in range(coins + 1):
                    if inPile >= pileSize:
                        break
                    cur = dpPiles[i][inPile]
                    last = dp[i-1][coins-inPile]
                    best = max(best, last + cur)
                dp[i][coins] = best
                
        return max(dp[n-1][:k + 1])

                
                
                
            
            