class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf') for _1 in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(n - 2, -1, -1):
            dp[m-1][i] = grid[m-1][i] + dp[m-1][i + 1]
        for j in range(m - 2, -1, -1):
            dp[j][n-1] = grid[j][n-1] + dp[j + 1][n-1]
            
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                cur = grid[r][c]
                dp[r][c] = min(cur + dp[i][j]
                              for i,j in [(r + 1, c), (r, c+ 1)]
                              if i < m and j < n)
        return dp[0][0]
                