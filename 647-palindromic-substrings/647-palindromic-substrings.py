class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            ans += 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1
                
        for length in range(3, n + 1):
            for st in range(n - length + 1):
                end = st + length - 1
                    
                if s[end] == s[st]:
                    isPali = dp[st + 1][end - 1]
                    dp[st][end] = isPali
                    if isPali:
                        ans += 1
                else:
                    dp[st][end] = False
        return ans
                
            