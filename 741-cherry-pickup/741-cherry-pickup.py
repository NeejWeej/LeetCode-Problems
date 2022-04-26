class Solution:
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 2 paths
        #dp[r1][r2], cur_time = t, 
        # c1 = n - 1 - (t - (n - 1 - r1))
        # = n - 1 - t + n - 1 - r1
        # = 2n - 2 - t - r1
        dp = [[float('-inf') for _1 in range(n)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*n - 1):
            nextt = [[float('-inf') for _1 in range(n)] for _ in range(n)]
            # print(dp, t)
            for r1 in range(max(0, t - (n - 1)), min(t, n - 1) + 1):
                for r2 in range(max(0, t - (n - 1)), min(t, n - 1) + 1):
                    if grid[r1][t - r1] == -1 or grid[r2][t - r2] == -1:
                        continue
                    cur = grid[r1][t-r1]
                    if r1 != r2:
                        cur += grid[r2][t-r2]
                    nextt[r1][r2] = max(cur + dp[i][j]
                                        for i in (r1-1,r1) for j in (r2-1, r2)
                                        if i >=0 and j>=0)
            dp = nextt
        print(dp)
        return dp[-1][-1] if dp[-1][-1] > 0 else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.ans = 0
        # # neighs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # n = len(grid)
        # if n == 1:
        #     return 1 if grid[0][0] == 1 else 0
        # def CP(down, collected, r, c):
        #     if r == 0 and c == 0 and not down:
        #         self.ans = max(collected, self.ans)
        #     had_cherry = False
        #     if grid[r][c] == 1:
        #         collected += 1
        #         had_cherry = True
        #         grid[r][c] = 0
        #     if down:
        #         neighs = [(0, 1), (1, 0)]
        #         for dx, dy in neighs:
        #             if r + dx == n-1 and c + dy == n - 1:
        #                 CP(False, collected, r + dx, c + dy)
        #             elif r+dx<n and c+dy<n and grid[r+dx][c+dy] != -1:
        #                 CP(True, collected, r + dx, c + dy)
        #     else:
        #         neighs = [(0, -1), (-1, 0)]
        #         for dx, dy in neighs:
        #             if 0<=r+dx and 0<=c+dy and grid[r+dx][c+dy] != -1:
        #                 CP(False, collected, r + dx, c + dy)
        #     if had_cherry:
        #         grid[r][c] = 1
        # CP(True, 0, 0, 0)
        # return self.ans
                
            
        