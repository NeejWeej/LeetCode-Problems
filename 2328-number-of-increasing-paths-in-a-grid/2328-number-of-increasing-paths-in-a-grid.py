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
                return self.dp[r][c][0]
            val = 1
            for dx, dy in directions:
                if 0 <= r+dx <m and 0<= c + dy<n:
                    if grid[r+dx][c+dy] > grid[r][c]:
                        val += dfs(r+dx, c + dy)
            self.dp[r][c] = [val, True]
            return val
        
        tot = 0
        for i in range(m):
            for j in range(n):
                tot += dfs(i,j)
                
        return tot % modVal
        
        
                
        
        