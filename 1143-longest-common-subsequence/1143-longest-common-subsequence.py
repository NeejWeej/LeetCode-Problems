class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)
        # if t1 < t2:
        #     text1, text2, t1, t2 = text2, text1, t2, t1
        
        dp = [ [0 for _ in range(t2 + 1)] for _ in range(t1 + 1)]

        for i in range(1, t1 + 1):
            for j in range(1, t2 + 1):
                best = dp[i-1][j-1]
                if text1[i - 1] == text2[j - 1]:
                    # if best == 0:
                    #     print(i,j)
                    dp[i][j] = 1 + best
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
                
                
        
#         t1 = len(text1)
#         t2 = len(text2)
#         dp = [[0 for i in range(t2 + 1)] for j in range(t1 + 1)]      
        
#         for i in range(1, t1 + 1):
#             for j in range(1, t2 + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 else:
#                     dp[i][j] = dp[i-1][j-1]
#         return dp[-1][-1]
        
        
        