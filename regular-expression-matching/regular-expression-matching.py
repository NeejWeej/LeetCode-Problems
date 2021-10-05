class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ans = False
        n = len(s)
        m = len(p)
        dp = [ [False]*(m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[j][0] = False
        i = 2
        while (i - 1) < m and p[i - 1] == '*':
            dp[0][i] = True
            i += 2
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    last_char = p[j - 2]
                    dp[i][j] = (dp[i - 1][j] and (s[i - 1] == last_char or last_char == '.'))
                    dp[i][j] = dp[i][j] or dp[i][j-2]
                else:
                    dp[i][j] = False
        ans = dp[-1][-1]            
        return ans
                