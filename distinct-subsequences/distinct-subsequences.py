class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return 1 if s == t else 0 
        dp = [[0]* (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(dp[0])):
            #this is the empty string
            dp[0][i] = 1
        for a in range(1, len(s) + 1):
            for b in range(1, len(t) + 1):
                if s[a - 1] == t[b-1]:
                    dp[b][a] = dp[b - 1][a - 1] + dp[b][a - 1]
                else:
                    dp[b][a] = dp[b][a - 1]
        return dp[-1][-1]
        # def recursiveDistinct(s, t):
        #     if len(s) < len(t):
        #         return 0
        #     if len(s) == len(t):
        #         return 1 if s == t else 0
        #     if t == '':
        #         return 1
        #     idx = 0
        #     while s[idx] != t[0]:
        #         idx += 1
        #     if s[0] != t[0]:
        #         return recursiveDistinct(s[1:], t)
        #     return recursiveDistinct(s[1:], t[1:]) \
        #         + recursiveDistinct(s[1:], t)
        # return recursiveDistinct(s,t)
        
        