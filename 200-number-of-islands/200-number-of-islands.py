class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def search(grid, x, y):
            grid[x][y] = "0"
            direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in direc:
                if 0<= x + dx < m and 0<= y+dy < n:
                    if grid[x+dx][y+dy] == "1":
                        search(grid, x+dx, y + dy)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    search(grid, i, j)
        return ans
        