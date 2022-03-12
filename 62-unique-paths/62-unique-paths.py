class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        dp[m-1][n-2] = 1
        dp[m-2][n-1] = 1
        
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                down = 0
                if x < m - 1:
                    down = dp[x + 1][y]
                right = 0
                if y < n - 1:
                    right = dp[x][y + 1]
                dp[x][y] = dp[x][y] + down + right
        return dp[0][0]