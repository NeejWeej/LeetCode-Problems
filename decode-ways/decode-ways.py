class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 0 if s[1] == '0' else 1
        # if int(s[:2]) <= 26:
        #     dp[1] += 1
            
        two_ago = 1
        one_ago = 0 if s[1] == '0' else 1
        
        if int(s[:2]) <= 26:
            one_ago += 1
        
        cur = one_ago
        for idx, val in enumerate(s[2:], 2):
            # single_digit = 0 if val == '0' else dp[idx - 1]
            
            single_digit = 0 if val == '0' else one_ago
            
            double = int(s[idx - 1: idx + 1])
            # double_digit = 0 if (double > 26 or s[idx-1] == '0') else dp[idx - 2]
            
            double_digit = 0 if (double > 26 or s[idx-1] == '0') else two_ago
            
            # dp[idx] = double_digit + single_digit
            cur = double_digit + single_digit
            two_ago = one_ago
            one_ago = cur
        return cur
        # return dp[-1]
    
        