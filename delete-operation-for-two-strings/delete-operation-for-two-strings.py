class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (n+1) for _ in range(m + 1)]
        
        for j in range(m + 1):
            dp[j][0] = j
        
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = 1 + min(dp[j-1][i], dp[j][i-1])
        
        return dp[-1][-1]