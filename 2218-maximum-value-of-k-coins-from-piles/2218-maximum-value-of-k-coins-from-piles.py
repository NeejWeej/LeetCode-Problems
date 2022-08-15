class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        
        val = 0
        firstPile = piles[0]
        firstDP = dp[0]
        
        for i in range(min(k + 1, len(firstPile))):
            firstDP[i] = val
            val += firstPile[i]
            
        if len(firstPile) < k + 1:
            firstDP[len(firstPile)] = val
        
        for i in range(1, n):
            pileSize = len(piles[i])
            
            for coins in range(k + 1):
                best = 0
                cur = 0
                for inPile in range(min(pileSize, coins + 1)):
                    last = dp[i-1][coins-inPile]
                    best = max(best, last + cur)
                    cur += piles[i][inPile]
                    
                if pileSize < coins + 1:
                    # we ended early, have to include final coin added
                    last = dp[i-1][coins - inPile - 1]
                    best = max(best, last + cur) 
                    
                dp[i][coins] = best
                
        return max(dp[n-1][:k + 1])

                
                
                
            
            