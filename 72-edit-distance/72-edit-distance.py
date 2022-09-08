class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n < m:
            n, m, word1, word2 = m, n, word2, word1
            
        if m == 0:
            return n
        
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 0
        for i in range(m + 1):
            dp[i][0] = i
            dp[0][i] = i
        
        for i in range(m + 1, n + 1):
            dp[i][0] = i
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
        