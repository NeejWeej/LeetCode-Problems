class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return max(n, m)
        
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 0
        for i in range(min(n,m) + 1):
            dp[i][0] = i
            dp[0][i] = i
        
        for i in range(min(n,m) + 1, max(n, m) + 1):
            if i <= n:
                dp[i][0] = i
            if i <= m:
                dp[0][i] = i
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
        print(dp)
        return dp[-1][-1]
        