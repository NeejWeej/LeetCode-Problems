class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        modVal = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        self.ans = 0
        self.dp = [[[1, False] for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(r, c):
            if self.dp[r][c][1]:
                return
            val = 1
            for dx, dy in directions:
                if 0 <= r+dx <m and 0<= c + dy<n:
                    if grid[r+dx][c+dy] > grid[r][c]:
                        dfs(r+dx, c + dy)
                        val += self.dp[r+dx][c+dy][0]
            self.dp[r][c] = [val, True]
        
        tot = 0
        for i in range(m):
            for j in range(n):
                dfs(i,j)
                tot += self.dp[i][j][0]
                
        return tot % modVal
        
        
                
        
        