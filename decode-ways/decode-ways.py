class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 0 if s[1] == '0' else 1
        if int(s[:2]) <= 26:
            dp[1] += 1
        for idx, val in enumerate(s[2:], 2):
            single_digit = 0 if val == '0' else dp[idx - 1]

            double = int(s[idx - 1: idx + 1])
            double_digit = 0 if (double > 26 or s[idx-1] == '0') else dp[idx - 2]
            
            dp[idx] = double_digit + single_digit
        return dp[-1]
            
        
        # n = len(s)
        # if (n == 1 and s[0] != '0') or n == 0:
        #     return 1
        # if s[0] == '0':
        #     return 0
        # first_two = int(s[:2])
        # ans = 0
        # ans += self.numDecodings(s[1:])
        # if 10 <= first_two and first_two <= 26:
        #     ans += self.numDecodings(s[2:])
        # return ans
    
        