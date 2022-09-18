class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        
        if n == 1:
            return 1
        
        dp = [0]*n
        if s[-1] != '0':
            dp[-1] = 1
        if s[-2] != '0':
            dp[-2] = dp[-1]
            if int(s[-2:]) <= 26:
                dp[-2] += 1
        
        enum =  enumerate(reversed(s))
        # do this to not copy a reversed form of the string
        next(enum)
        next(enum)
        
        for revI, val in enum:
            i = n - revI - 1
            if val != '0':
                dp[i] = dp[i + 1]
                if int(val + s[i + 1]) <= 26:
                    dp[i] += dp[i + 2]
                    
        return dp[0]
        