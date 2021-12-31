class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)
        dp = [[0 for i in range(t2 + 1)] for j in range(t1 + 1)]      
        
        for i in range(1, t1 + 1):
            for j in range(1, t2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        # print(dp)
        return dp[-1][-1]
        
        
        